class Groups:
    def __init__(self, client):
        self.client = client
    
    def create(self, group):
        """ Creates a new group

        :param group: Group data. Refer to: https://docs.microsoft.com/en-us/graph/api/group-post-groups?view=graph-rest-1.0
        :type group: dict
        :returns: The data of the new group, including its new id
        :rtype: dict
        :raises: Exception
        """
        path = '/groups'
        return self.client.post(path, group)

    def find_all(self, params={}, **options):
        """ Fetches all groups

        :returns: A list containing all groups
        :rtype: list of dict
        :raises: Exception
        """
        path = '/groups'
        return self.client.get_collection(path)
    
    def find_by_id(self, id, params={}, **options):
        """ Fetches a group by id

        :returns: Group data
        :rtype: dict
        :raises: Exception
        """
        path = '/groups/' + id
        return self.client.get(path)