from sugar.datastore import datastore
from datetime import date
import json
import os


class badges:

    def __init__(self, activity, bundle_id):

        self._id = bundle_id
        ds_objects, num_objects = datastore.find({'activity': activity})

        # Path for all badges
        badge_path = os.path.expanduser('~/.local/share/badges')

        # Creates a new directory for badges if one doesn't exist
        try:
            os.makedirs(badge_path)

        # Directory already exists
        except OSError:
            pass

        # Destination path for the activity's badges
        dest = os.path.join(badge_path, self._id)
        # Source path for the activity's local badges
        source = os.path.abspath('badges/')

        # Create a new directory for badges for this activity if none exist
        try:
            if not os.path.exists(dest):
                os.symlink(source, dest)

        # Directory already exists
        except OSError:
            pass

        # Create a datastore object for this activity if one doesn't exist
        if not ds_objects:
            self._list = datastore.create()
            self._list.metadata['activity'] = activity
            self._list.metadata['has_badges'] = 'True'
            self._list.metadata['badge_list'] = json.dumps({})
            datastore.write(self._list)
        else:
            self._list = ds_objects[0]

    def award(self, name, description):
        """
        Awards a badge in an activity

        :type name: string
        :param name: The name of the badge

        :type description: string
        :param description: The description of the badge
        """

        badge_json = json.loads(self._list.metadata['badge_list'])

        # Check if the badge has already been acquired
        if not name in badge_json.keys():

            # Generate the badge's info
            today = date.today()
            badge_info = {'name': name,
                          'criteria': description,
                          'time': today.strftime("%m/%d/%y"),
                          'bundle_id': self._id}

            badge_json[name] = badge_info

            # Save the new badge info to the DS object
            self._list.metadata['badge_list'] = json.dumps(badge_json)
            datastore.write(self._list)

    def clear(self):
        """
        Clears all of the badges that have been awarded by an activity
        WARNING: badges will be lost forever, used to testing purposes
        """
        self._list.destory()
        datastore.delete(self._list.object_id)
