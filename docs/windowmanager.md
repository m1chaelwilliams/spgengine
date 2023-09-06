# SPG Window Manager

Houses the pygame screen instance aswell as an optional "proxy screen".


## Method List

```py
WindowManager(screen: pygame.Surface)
```
 - Creates `WindowManager` instance.
 - Stores screen variable
 - Creates empty variables for `proxy_screen`, `proxy_scale`, `proxy_flags`

```py
config_window(self, size: tuple[int, int], *flags) -> pygame.Surface
```
 - reassigns `screen` to a new pygame display.

```py
create_proxy_screen(self, size: tuple[int, int], *flags) -> pygame.Surface
```
 - Creates surface and stores it in `proxy_screen` variable.
 - Assigns `proxy_scale` and `proxy_flags`

```py
close(self) -> None
```
 - Sends a `close_requested` event to `EventManager` statically.

```py
get_proxy_mouse_pos(self) -> tuple[int, int]
```
 - Returns mouse position adjusting screen coordinates to proxy screen coordinates.