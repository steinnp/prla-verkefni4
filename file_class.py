class File_info:
    def __init__(self, old_file_position, name = None, season = None, episode = None,
                 episode_name = None):
        self.old_file_position = old_file_position
        self.name = name
        self.season = season
        self.episode = episode
        self.episode_name = episode_name

    def set_name(self, name):
        self.name = name

    def set_season(self, season):
        self.season = season

    def set_episode(self, episode):
        self.episode = episode

    def set_episode_name(self, episode_name):
        self.episode_name = episode_name

    def get_name(self):
        return self.name

    def get_season(self):
        return self.season

    def get_episode(self):
        return self.episode

    def get_episode_name(self):
        return self.episode_name
