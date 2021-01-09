import json

from django.http import JsonResponse

from core import models


def operations(request):
    req_key = request.POST.get('key')

# ****************************************************************************

    if req_key == 'delete_messages':
        deleted_message_list = request.POST.get('deleted_message_list')
        messages = models.Message.objects.filter(pk__in=json.loads(deleted_message_list))
        if request.user.is_authenticated:
            for message in messages:
                message.is_deleted = True
                message.save()
            return JsonResponse({'details': 'Deleted selected messages'})
        else:
            return JsonResponse({'message': 'You can not change this information!'})

# ****************************************************************************

    if req_key == 'delete_trash_messages':
        deleted_message_list = request.POST.get('deleted_message_list')
        messages = models.Message.objects.filter(pk__in=json.loads(deleted_message_list))
        if request.user.is_authenticated:
            for message in messages:
                message.delete()
            return JsonResponse({'details': 'Deleted selected messages'})
        else:
            return JsonResponse({'message': 'You can not change this information!'})

    # ****************************************************************************

    if req_key == 'load_staff_list':
        staff = models.Staff.objects.filter(is_deleted=False)
        staff_list = []
        for stf in staff:
            staff_list.append({
                'pk' : stf.pk,
                'name' : stf.name,
                'branch' : stf.branch.name,
            })

        return JsonResponse(staff_list,safe=False)

# ****************************************************************************
    if req_key =='delete_staff':
        pk = request.POST.get('pk')
        if not models.Staff.objects.filter(pk=pk).exists():
            return JsonResponse({'details': 'STAFF NOT FOUND'}, status=404)
        if request.user.is_superuser:
            staff = models.Staff.objects.get(pk=pk)
            staff.is_deleted = True
            staff.save()
            return JsonResponse({'details': 'STAFF DELETED'})
        else:
            return JsonResponse({'message': 'You can not change this information!'})

# ****************************************************************************

    if req_key == 'add_staff':
        name = request.POST.get('name')
        short_name = request.POST.get('short_name')
        branch = request.POST.get('branch')

        if not name or not short_name or not branch:
            return JsonResponse({'details': 'Please fill all fields'},status=400)
        if name.isdigit() or short_name.isdigit():
            return JsonResponse({'details':'Do not use numbers,please'},status=400)


        models.Staff.objects.create(
            name=name,
            short_name=short_name,
            branch_id=branch,
        )
        return JsonResponse({'details':'Staff added'})

# ****************************************************************************

    if req_key == 'get_staff':
        pk = request.POST.get('pk')

        if not models.Staff.objects.filter(pk=pk).exists():
            return JsonResponse({'details':'STAFF NOT FOUND'},status=404)

        staff = models.Staff.objects.get(pk=pk)
        staff = {
            'pk' : staff.pk,
            'name' : staff.name,
            'branch' : staff.branch_id,
            'short_name' : staff.short_name,
        }

        return  JsonResponse(staff, safe= False)

# ****************************************************************************

    if req_key == 'update_staff':
        pk = request.POST.get('pk')
        staffs = models.Staff.objects.filter(is_deleted=False)

        if not models.Staff.objects.filter(pk=pk).exists():
            return JsonResponse({'details': 'STAFF NOT FOUND'}, status=404)

        staff = staffs.get(pk=pk)

        name = request.POST.get('name')
        short_name = request.POST.get('short_name')
        branch = request.POST.get('branch')

        if not name or not short_name or not branch:
            return  JsonResponse({'details': 'inputs not valid'},status=404)


        staff.name = name
        staff.short_name = short_name
        staff.branch_id = branch
        staff.save()

        return JsonResponse({'details': 'STAFF UPDATED'})

# ****************************************************************************

    return JsonResponse({'details' : 'Request received'}, status=403)