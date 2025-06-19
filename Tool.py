@dataclass
class Tool:
    name: str
    description: str
    func: Callable[..., str]
    parameters: Dict[str, Dict[str, str]]
    
    def __call__(self, *args, **kwargs) -> str:
        return self.func(*args, **kwargs)