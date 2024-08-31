from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from .forms import cutsForm, UserRegistrationForm, UserAuthenticationForm, sizesFormSet, colorsFormSet, linesFormSet, jobsForm
from django.utils.html import strip_tags
from .models import cuts, colors, sizes, lines, amounts, jobs
from django.http import JsonResponse


def registerf(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('workshop:index')
        else:
            for error in form.errors.items():
                messages.error(request, f'{strip_tags(error[1])}')
            return redirect('workshop:register')
    else:
        if not request.user.is_authenticated:
            form = UserRegistrationForm()
            return render(request, 'workshop/register.html', {'form': form})
        else:
            return redirect('workshop:index')



def loginf(request):
    if request.method == "POST":
        form = UserAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('workshop:index')
        else:
            for error in form.errors.items():
                messages.error(request, f'{strip_tags(error[1])}')
            return redirect('workshop:login')
    
    else:
        if not request.user.is_authenticated:
            form = UserAuthenticationForm(request)
            return render(request, 'workshop/login.html', {'form': form})
        else:
            return redirect('workshop:index')



@login_required
def indexf(request):
    jobs_at_hand = jobs.objects.filter(completed = False).order_by('-id')[:15]

    cuts_objects = cuts.objects.all()
    cuts_and_percentages = []

    latest_finished= cuts.objects.filter(completed = True)

    for cut_instance in cuts_objects:
        number_of_colors = cut_instance.colors_set.count()
        number_of_unfinished_colors = cut_instance.colors_set.filter(completed = False).count()

        if number_of_colors > 0:
            percentage = (1 - (number_of_unfinished_colors / number_of_colors)) * 100

        else:
            percentage = 0
        cuts_and_percentages.append({cut_instance.cut: int(percentage)})

    return render(request, 'workshop/index.html', {'jobsAtHand': jobs_at_hand, 'cutsPercentage': cuts_and_percentages, 'latestFinished': latest_finished})



@staff_member_required(login_url='workshop:login')
def newcutf(request):
    if request.method == "POST":
        cuts_in = cutsForm(request.POST)
        if cuts_in.is_valid():
            new_cut = cuts_in.save()  # Save the new cut instance and capture it
            amounts.objects.create(cut=new_cut) # Creating a new amounts table for this cut
        else:
            messages.error(request, 'فرم ارسال شده صحیح نیست!')


        sizes_in = sizesFormSet(request.POST, prefix='sizes')
        if sizes_in.is_valid():
            for form in sizes_in:
                size_instance = form.save(commit=False)  # Save the size instance without committing to the database
                size_instance.cut = new_cut  # Set the cut foreign key to the new cut instance
                size_instance.save()  # Save the size instance with the updated foreign key

                colors_in = colorsFormSet(request.POST, prefix='colors')
                if colors_in.is_valid():
                    for form in colors_in:
                        color_instance = form.save(commit=False)  # Save the color instance without committing to the database
                        color_instance.cut = new_cut  # Set the cut foreign key to the new cut instance
                        color_instance.size = size_instance
                        color_instance.save()  # Save the color instance with the updated foreign key

                        lines_in = linesFormSet(request.POST, prefix='lines')
                        if lines_in.is_valid():
                            for form in lines_in:
                                line_instance = form.save(commit=False)  # Save the line instance without committing to the database
                                line_instance.cut = new_cut  # Set the cut foreign key to the new cut instance
                                line_instance.size = size_instance
                                line_instance.color = color_instance
                                line_instance.cut = new_cut
                                line_instance.save()  # Save the line instance with the updated foreign key
                        else:
                            messages.error(request, 'خط‌های ارسال شده صحیح نیست!')
                            return redirect('workshop:newcut')
                else:
                    messages.error(request, 'رنگ‌های ارسال شده صحیح نیست!')
                    return redirect('workshop:newcut')
        else:
            messages.error(request, 'سایزهای ارسال شده صحیح نیست!')
            return redirect('workshop:newcut')

                
        messages.success(request, 'برش جدید با موفقیت ثبت شد.')
        return redirect('workshop:index')
    else:
        cuts_out = cutsForm(initial={'colortype': 'رنگی', 'sizetype': 'بزرگسال'})
        colors_out = colorsFormSet(prefix='colors')
        sizes_out = sizesFormSet(prefix='sizes')
        lines_out = linesFormSet(prefix='lines')
        return render(request, 'workshop/newcut.html', {'cutsForm': cuts_out, 'sizesFormSet': sizes_out, 'colorsFormSet': colors_out, 'linesFormSet': lines_out})



@staff_member_required(login_url='workshop:login')
def newjobf(request):
    if request.method == "POST":
        jobs_in = jobsForm(request.POST)
        if jobs_in.is_valid():
            jobs_in.save()
            messages.success(request, 'کار جدید با موفقیت ثبت شد.')
            return redirect('workshop:index')
        else:
            messages.error(request,'فرم ارسال شده صحیح نیست.')
            return redirect('workshop:newjob')
    else:
        jobs_out = jobsForm()
        return render(request, 'workshop/newjob.html', {'jobs': jobs_out,})



# Fetch API view for the NewJob page
def newjob_sizes(request, selected_cut):
    related_sizes = sizes.objects.filter(cut_id = selected_cut, completed = False)
    serialized_sizes = [{'id': size.id, 'size': size.size} for size in related_sizes]

    return JsonResponse({'sizes': serialized_sizes})


def newjob_colors(request, selected_size):
    related_colors = colors.objects.filter(size_id = selected_size, completed = False)
    serialized_colors = [{'id': color.id, 'color': color.color} for color in related_colors]

    return JsonResponse({'colors': serialized_colors})


def newjob_lines(request, selected_color):
    related_lines = lines.objects.filter(color_id = selected_color, completed = False)
    serialized_lines = [{'id': line.id, 'line': line.line} for line in related_lines]

    return JsonResponse({'lines': serialized_lines})




@staff_member_required(login_url='workshop:login')
def salaryf(request):
    return render(request, 'workshop/salary.html')



def logoutf(request):
    logout(request)
    return redirect('workshop:login')