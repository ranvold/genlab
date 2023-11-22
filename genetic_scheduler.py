from dataclasses import dataclass
import random

POPULATION_SIZE = 100
MUTATION_RATE = 0.1
GENERATIONS = 100

@dataclass
class Class:
    subject: str
    teacher: str
    group: str
    time: int
    day: int


class GeneticScheduler:
    def __init__(self, subjects, teachers, groups, classes_per_day, days_per_week):
        self.subjects = subjects
        self.teachers = teachers
        self.groups = groups
        self.classes_per_day = classes_per_day
        self.days_per_week = days_per_week

    def generate_random_schedule(self):
        schedule = []
        for _ in range(self.days_per_week * len(self.groups)):
            subject = random.choice(self.subjects)
            time = random.randint(1, self.classes_per_day)
            teacher = random.choice(self.teachers)
            group = random.choice(self.groups)
            day = random.randint(1, self.days_per_week)
            schedule.append(Class(subject, teacher, group, time, day))
        return schedule

    def generate_random_population(self, population_size):
        return [self.generate_random_schedule() for _ in range(population_size)]

    @staticmethod
    def calculate_fitness(schedule):
        teacher_conflicts = sum(1 for i in range(len(schedule)) for j in range(i + 1, len(schedule))
                                if
                                schedule[i].teacher == schedule[j].teacher and schedule[i].time == schedule[j].time and
                                schedule[i].day == schedule[j].day)
        group_conflicts = sum(1 for i in range(len(schedule)) for j in range(i + 1, len(schedule)) if
                              schedule[i].group == schedule[j].group and schedule[i].time == schedule[j].time and
                              schedule[i].day == schedule[j].day)
        total_conflicts = teacher_conflicts + group_conflicts
        return 1.0 / (1.0 + total_conflicts)

    def mutate(self, schedule):
        if random.random() < MUTATION_RATE:
            random_class_index = random.randint(0, len(schedule) - 1)
            schedule[random_class_index] = Class(
                random.choice(self.subjects),
                random.choice(self.teachers),
                random.choice(self.groups),
                random.randint(1, self.classes_per_day),
                random.randint(1, self.days_per_week)
            )
        return schedule

    @staticmethod
    def crossover(schedule1, schedule2):
        crossover_point = random.randint(1, len(schedule1) - 1)
        child1 = schedule1[:crossover_point] + schedule2[crossover_point:]
        child2 = schedule2[:crossover_point] + schedule1[crossover_point:]
        return child1, child2

    @staticmethod
    def select_best(population, fitness_scores):
        best_index = max(range(len(population)), key=lambda i:
            fitness_scores[i])
        return population[best_index], fitness_scores[best_index]

    def solve(self):
        population = self.generate_random_population(POPULATION_SIZE)
        best_schedule = None
        best_fitness_score = 0
        for _ in range(GENERATIONS):
            fitness_scores = [self.calculate_fitness(schedule) for schedule in population]
            best_schedule, best_fitness_score = self.select_best(population, fitness_scores)
            new_population = []
            while len(new_population) < POPULATION_SIZE:
                parent1, parent2 = random.choices(population, weights=fitness_scores, k=2)
                child1, child2 = self.crossover(parent1, parent2)
                new_population.extend([self.mutate(child1), self.mutate(child2)])
            population = new_population
        return best_schedule, best_fitness_score