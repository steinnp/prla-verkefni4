class File_info:
    def __init__(self, old_file_position, name = None, season = None, episode = None,
                 episode_name = None, extension = None, new_file_position = None,
                 new_name = None):
        self.old_file_position = old_file_position
        if not name == None:
            self.name = name.strip()
        else:
            self.name = name
        if not season == None:
            self.season = season.strip()
        else:
            self.season = season
        if not episode == None:
            self.episode = episode.strip()
        else:
            self.episode = episode
        if not episode_name == None:
            self.episode_name = episode_name.strip()
        else:
            self.episode_name = episode_name
        if not extension == None:
            self.extension = extension.strip()
        else:
            self.extension = extension
        self.new_file_position = new_file_position
        self.new_name = new_name

    def set_old_file_position(self, position):
        self.old_file_position = position

    def set_name(self, name):
        self.name = name.strip()

    def set_season(self, season):
        self.season = season.strip()

    def set_episode(self, episode):
        self.episode = episode.strip()

    def set_episode_name(self, episode_name):
        self.episode_name = episode_name.strip()

    def set_extension(self, extension):
        self.extension = extension.strip()

    def set_new_file_position(self, position):
        self.new_file_position = position

    def set_new_name(self, name):
        self.new_name = name

    def get_name(self):
        return self.name

    def get_season(self):
        return self.season

    def get_episode(self):
        return self.episode

    def get_episode_name(self):
        return self.episode_name

    def get_extension(self):
        return self.extension

    def get_old_file_position(self):
        return self.old_file_position

    def get_new_file_position(self):
        return self.new_file_position

    def get_new_name(self):
        return self.new_name
