class ProjectInclude:
    def __init__(self):
        self.includes = list()
    def add(self, include):
        if isinstance(include, list):
                self.includes.extend(include)
        if isinstance(include, str):
            self.includes.append(include)
    
    def empty(self):
        if self.includes:
            return True
        else:
            return False

    def __repr__(self):
        return  str(self.includes)