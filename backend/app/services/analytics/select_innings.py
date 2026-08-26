from app.models.analytic import InningsScope

def select_innings(innings, scope):

    if scope == InningsScope.ALL:
        return innings
        
    return [
        inning
        for inning in innings
        if inning.innings_type == scope
    ]        

