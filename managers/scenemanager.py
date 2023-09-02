class SceneManager:
    active_scene: str = ""
    previous_scene: str = ""
    @staticmethod
    def set_scene(new_scene: str) -> None:
        SceneManager.previous_scene = SceneManager.active_scene
        SceneManager.active_scene = new_scene
    @staticmethod
    def get_scene() -> str:
        return SceneManager.active_scene