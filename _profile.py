# Profile.py

class Profile:
    def __init__(self, name, favorite_language, hobby, tech_stack, github_username, fun_fact):
        self.name = name
        self.favorite_language = favorite_language
        self.hobby = hobby
        self.tech_stack = tech_stack  # should be a list
        self.github_username = github_username
        self.fun_fact = fun_fact

    def __str__(self):
        return (
            f"👤 Profile\n"
            f"Name: {self.name}\n"
            f"Favorite Language: {self.favorite_language}\n"
            f"Hobby: {self.hobby}\n"
            f"Tech Stack: {', '.join(self.tech_stack)}\n"
            f"GitHub: https://github.com/{self.github_username}\n"
            f"Fun Fact: {self.fun_fact}\n"
        )


# Example usage
if __name__ == "__main__":
    my_profile = Profile(
        name="Alice Doe",
        favorite_language="Python",
        hobby="Photography",
        tech_stack=["Python", "Django", "Git", "Docker"],
        github_username="alice-doe",
        fun_fact="I can solve a Rubik's cube in under a minute!"
    )

    print(my_profile) 
