class HasAccessMixin(object):

    def has_access(self, user, action=None):
        """
        :param user:
        :param action:
        :return [bool, bool] - first bool is condition to access,
        second is check to a final condition - good to inheritance:
        """
        action = action or self.action

        if not user.is_authenticated:
            return False, True

        if user.is_superuser:
            return True, True

        if not user.has_perm('calendars.%s_event' % action):
            return False, True

        return True, False


class HasAccessWithOrganizerMixin(HasAccessMixin):

    def has_access(self, user, action=None):
        obj = self.get_object()
        has_access, final = super().has_access(user, action)
        if final:
            return has_access, True

        print(obj.user)
        return obj.user and obj.user.pk == user.pk, False