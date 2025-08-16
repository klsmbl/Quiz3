from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import JobOpening, JobApplicant
from .forms import JobApplyForm



def job_list(request):
    jobs = JobOpening.objects.all()
    query = request.GET.get('q')
    if query:
        jobs = jobs.filter(
            Q(job_title__icontains=query) |
            Q(job_description__icontains=query) |
            Q(location__icontains=query)
        ).distinct()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})


@login_required
def job_detail(request, pk):
    job = get_object_or_404(JobOpening, pk=pk)
    apply_form = JobApplyForm()

    if request.user.is_admin:
        applicants = JobApplicant.objects.filter(job=job)
        return render(request, 'jobs/job_detail.html', {'job': job, 'applicants': applicants, 'is_admin': True})
    else:

        has_applied = JobApplicant.objects.filter(user=request.user, job=job).exists()
        return render(request, 'jobs/job_detail.html',
                      {'job': job, 'apply_form': apply_form, 'has_applied': has_applied, 'is_admin': False})


@login_required
def apply_for_job(request, pk):
    job = get_object_or_404(JobOpening, pk=pk)
    if not request.user.is_admin:
        if request.method == 'POST':
            form = JobApplyForm(request.POST, request.FILES)
            if form.is_valid():
                # Check if the user has already applied for this job
                if JobApplicant.objects.filter(user=request.user, job=job).exists():
                    messages.error(request, 'You have already applied for this job.')
                    return redirect('job_detail', pk=pk)

                job_applicant = form.save(commit=False)
                job_applicant.user = request.user
                job_applicant.job = job
                job_applicant.save()
                messages.success(request, 'Your application has been submitted successfully!')
                return redirect('job_detail', pk=pk)
        messages.error(request, 'Invalid form submission.')
    else:
        messages.error(request, 'Admins cannot apply for jobs.')
    return redirect('job_detail', pk=pk)


class JobUpdateView(UpdateView):
    model = JobOpening
    fields = ['job_title', 'job_description', 'min_offer', 'max_offer', 'location']
    template_name = 'jobs/job_form.html'
    success_url = reverse_lazy('job_list')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not self.request.user.is_admin:
            messages.error(self.request, "You are not authorized to edit this job post.")
            return redirect('job_list')
        return obj

    def form_valid(self, form):
        messages.success(self.request, "Job post updated successfully!")
        return super().form_valid(form)


class JobDeleteView(DeleteView):
    model = JobOpening
    template_name = 'jobs/job_confirm_delete.html'
    success_url = reverse_lazy('job_list')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not self.request.user.is_admin:
            messages.error(self.request, "You are not authorized to delete this job post.")
            return redirect('job_list')
        return obj

    def form_valid(self, form):
        messages.success(self.request, "Job post deleted successfully!")
        return super().form_valid(form)


from django.shortcuts import render

# Create your views here.
