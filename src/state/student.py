class Student:
    def __init__(self, student_id, subjects_and_classes, subject_targets, subject_give_ins, buddies):
        self.student_id = student_id  # Id of the student
        self.subjects_and_classes = subjects_and_classes  # Dict with subject as a key and class as value
        self.subject_targets = subject_targets  # Dict with subject as key and a list of target classes as value
        self.subject_give_ins = subject_give_ins  # Dict with subject as key and a list of give ins classes as value
        self.buddies = buddies  # Dict where for each subject (key) there is a list of ups ordered by their priority

    def add_subject_and_class(self, subject_name, class_number):
        if len(self.subjects_and_classes) < 7:  # TODO: review this line. Limit of 7 subjects for each student?
            self.subjects_and_classes[subject_name] = class_number
            return True
        return False

    def add_subject_target(self, subject_name, class_number):
        if subject_name in self.subjects_and_classes:
            if subject_name not in self.subject_targets:
                self.subject_targets[subject_name] = [class_number]
            else:
                self.subject_targets[subject_name].append(class_number)
            return True
        return False

    def remove_subject_target(self, subject_name):
        if subject_name in self.subject_targets:
            del self.subject_targets[subject_name]
            return True
        return False

    def remove_subject_target_class(self, subject_name, class_number):
        if subject_name in self.subject_targets and class_number in self.subject_targets[subject_name]:
            self.subject_targets[subject_name].remove(class_number)
            return True
        return False

    def add_subject_give_in(self, subject_name, class_number):

        if subject_name in self.subjects_and_classes:
            if subject_name not in self.subject_give_ins:
                self.subject_give_ins[subject_name] = [class_number]
            else:
                self.subject_give_ins[subject_name].append(class_number)
            return True
        return False

    def remove_subject_give_in(self, subject_name):
        if subject_name in self.subject_give_ins:
            del self.subject_give_ins[subject_name]
            return True
        return False

    def remove_subject_give_in_class(self, subject_name, class_number):
        if subject_name in self.subject_give_ins and class_number in self.subject_give_ins[subject_name]:
            self.subject_give_ins[subject_name].remove(class_number)
            return True
        return False

    def add_buddie(self, subject_name, buddie_up):
        if subject_name in self.subjects_and_classes:
            if subject_name not in self.buddies:
                self.buddies[subject_name] = [buddie_up]
            else:
                self.buddies[subject_name].append(buddie_up)
            return True
        return False

    def remove_buddie(self, subject_name):
        if subject_name in self.buddies:
            del self.buddies[subject_name]
            return True
        return False

    def remove_buddie_class(self, subject_name, buddie_up):
        if subject_name in self.buddies and buddie_up in self.buddies[subject_name]:
            self.buddies[subject_name].remove(buddie_up)
            return True
        return False

    def add_buddies(self, subject_name, buddies_up):
        if subject_name in self.subjects_and_classes:
            if subject_name in self.buddies:
                for buddy in buddies_up:
                    if buddy not in self.buddies[subject_name]:
                        self.buddies[subject_name].append(buddy)

            else:
                self.buddies[subject_name] = buddies_up

    def get_class_for_subject(self, subject):
        if subject in self.subjects_and_classes:
            return self.subjects_and_classes[subject]
        return None

    def set_class_for_subject(self, subject, subject_class):
        if subject in self.subjects_and_classes:
            self.subjects_and_classes[subject] = subject_class

    def get_targets_for_subject(self, subject):
        if subject in self.subject_targets:
            return self.subject_targets[subject]
        return None

    def __str__(self):
        return "\nID: " + str(self.student_id) + "\nClasses: " + str(
            self.subjects_and_classes) + "\nTarget Classes: " + str(self.subject_targets) + "\nGive ins" + str(
            self.subject_give_ins)

    def get_giveins_for_subject(self, subject):
        if subject in self.subject_give_ins:
            return self.subject_give_ins[subject]
        return None

    def __eq__(self, x):
        return self.student_id == x.student_id
