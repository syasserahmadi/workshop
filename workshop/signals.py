from workshop.models import cuts, colors, sizes, lines, amounts, jobs
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver



# Updating the amounts table when colors, sizes, or lines tables are saved or deleted
@receiver([post_save, post_delete], sender = colors)
def update_amounts_colors(sender, instance, **kwargs):
    amounts_instance = instance.cut.amounts
    if amounts_instance:
        distinct_colors = instance.cut.colors_set.values('color').distinct().count()
        amounts_instance.totalcolors = distinct_colors
        amounts_instance.save()


@receiver([post_save, post_delete], sender = sizes)
def update_amounts_sizes(sender, instance, **kwargs):
    amounts_instance = instance.cut.amounts
    if amounts_instance:
        amounts_instance.totalsizes = instance.cut.sizes_set.distinct().count()
        amounts_instance.save()


@receiver([post_save, post_delete], sender = lines)
def update_amounts_lines(sender, instance, **kwargs):
    amounts_instance = instance.cut.amounts
    if amounts_instance:
        amounts_instance.totallines = instance.cut.lines_set.distinct().count()
        amounts_instance.save()



# Changing completed boolean for lines, colors, sizes and cuts when saving or deleting jobs instance
@receiver(pre_save, sender = jobs)
def jobs_save_update(sender, instance, **kwargs):
    if instance.line_id:
        instance.line.completed = True
        instance.line.save()

    instance_color = instance.color
    instance_color_lines_set = instance.color.lines_set.all()

    incomplete_lines = 0
    for line in instance_color_lines_set:
        if line.completed == False:
            incomplete_lines += 1

    if incomplete_lines == 0:
        instance_color.completed = True
        instance_color.save()
    


    instance_size = instance.size
    instance_size_colors_set = instance.size.colors_set.all()

    incomplete_colors = 0
    for color in instance_size_colors_set:
        if color.completed == False:
            incomplete_colors += 1

    if incomplete_colors == 0:
        instance_size.completed = True
        instance_size.save()


    instance_cut = instance.cut
    instance_cut_sizes_set = instance.cut.sizes_set.all()

    incomplete_sizes = 0
    for size in instance_cut_sizes_set:
        if size.completed == False:
            incomplete_sizes += 1
    
    if incomplete_sizes == 0:
        instance_cut.completed = True
        instance_cut.save()


"""
@receiver(post_delete, sender = jobs)
def jobs_delete_update(sender, instance, **kwargs):
    if instance.line_id:
        instance.line.completed = False
        instance.line.save()



# If all of the lines in a color are done, set that color to complete
@receiver(post_save, sender = jobs)
def lines_in_colors(sender, instance, **kwargs):
    remaining_lines = instance.line.filter(completed = False)
    if remaining_lines:
        for color in remaining_lines:
            color.completed = True
            color.save()


# If there were no colors to sew in a cut instance, set that cut to completed
@receiver([post_save, post_delete], sender = jobs)
def cuts_completed_update(sender, instance, **kwargs):
    incomplete_colors = instance.cut.colors_set.filter(completed=False)

    if not incomplete_colors.exists():
        instance.cut.completed = True
        instance.cut.save()
"""
