class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """Initialize the television with default settings."""
        self._status: bool = False
        self._muted: bool = False
        self._volume: int = Television.MIN_VOLUME
        self._channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """Turn the TV on or off."""
        self._status = not self._status

    def mute(self) -> None:
        """Mute or unmute the TV."""
        if self._status:
            self._muted = not self._muted

    def channel_up(self) -> None:
        """Increase the TV channel."""
        if self._status:
            self._channel = (self._channel + 1) % (Television.MAX_CHANNEL + 1)

    def channel_down(self) -> None:
        """Decrease the TV channel."""
        if self._status:
            self._channel = (self._channel - 1) if self._channel > Television.MIN_CHANNEL else Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """Increase the TV volume."""
        if self._status:
            if self._muted:
                self._muted = False
            if self._volume < Television.MAX_VOLUME:
                self._volume += 1

    def volume_down(self) -> None:
        """Decrease the TV volume."""
        if self._status:
            if self._muted:
                self._muted = False
            if self._volume > Television.MIN_VOLUME:
                self._volume -= 1

    def __str__(self) -> str:
        """Return the TV's status, channel, and volume."""
        return f"Power {'On' if self._status else 'Off'}, Channel {self._channel}, Volume {self._volume}"

