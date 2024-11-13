# Import all components for easier access
from .home import show as home_show
from .experience import show as experience_show
from .projects import show as projects_show
from .education import show as education_show
from .skills import show as skills_show

# Export all shows for easier imports
__all__ = ['home_show', 'experience_show', 'projects_show', 'education_show', 'skills_show'] 