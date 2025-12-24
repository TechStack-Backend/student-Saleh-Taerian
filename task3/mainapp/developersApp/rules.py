import rules

@rules.predicate(bind=True)
def is_profile_owner(user ,profile):
    if profile is not None and user.profile == profile:
        return True
    return False

# @rules.predict(bind =True)
# def can_edit_own_profile(self , user , profile):
#     return user.has_perm('')

@rules.predicate(bind=True)
def is_project_owner(user, project):
    flag=0
    for proj in user.project:
        if proj==project:
            flag=1
    return project is not None and flag==1
        
rules.add_perm('developersApp.can_edit_own_profile' , is_profile_owner)
rules.add_perm('developersApp.can_edit_own_Prject' , is_project_owner)
