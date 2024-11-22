class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """Initialize the television with default settings."""
        self._status = False
        self._muted = False
        self._volume = Television.MIN_VOLUME
        self._channel = Television.MIN_CHANNEL

    def power(self):
        """Turn the TV on or off."""
        self._status = not self._status

    def mute(self):
        """Mute or unmute the TV."""
        if self._status:
            self._muted = not self._muted
            if self._muted:
                self._previous_volume = self._volume  # Save the current volume before muting
                self._volume = Television.MIN_VOLUME
            else:
                self._volume = self._previous_volume  # Restore the volume when unmuting

    def channel_up(self):
        """Increase the TV channel."""
        if self._status:
            self._channel = (self._channel + 1) % (Television.MAX_CHANNEL + 1)

    def channel_down(self):
        """Decrease the TV channel."""
        if self._status:
            self._channel = (self._channel - 1) if self._channel > Television.MIN_CHANNEL else Television.MAX_CHANNEL

    def volume_up(self):
        """Increase the TV volume."""
        if self._status:
            if self._muted:
                self.mute()  # Unmute if volume control is used
            if self._volume < Television.MAX_VOLUME:
                self._volume += 1

    def volume_down(self):
        """Decrease the TV volume."""
        if self._status:
            if self._muted:
                self.mute()  # Unmute if volume control is used
            if self._volume > Television.MIN_VOLUME:
                self._volume -= 1

    def __str__(self):
        """Return the TV's status, channel, and volume."""
        return f"Power {'On' if self._status else 'Off'}, Channel {self._channel}, Volume {self._volume}"
