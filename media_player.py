import pyglet

class MediaPlayer:
    def __init__(self):
        self.player = pyglet.media.Player()

    def load_file(self, file_path):
        media_source = pyglet.media.load(file_path)
        self.player.queue(media_source)

    def play(self):
        if not self.player.playing:
            self.player.play()

    def pause(self):
        if self.player.playing:
            self.player.pause()

    def stop(self):
        if self.player.playing:
            self.player.pause()
            self.player.seek(0)

    def skip_forward(self, seconds=10):
        if self.player.playing:
            current_time = self.player.time
            self.player.seek(current_time + seconds)

    def skip_backward(self, seconds=10):
        if self.player.playing:
            current_time = self.player.time
            new_time = max(current_time - seconds, 0)
            self.player.seek(new_time)

    def change_volume(self, value):
        self.player.volume = value / 100  # Normalize volume to 0.0 - 1.0
