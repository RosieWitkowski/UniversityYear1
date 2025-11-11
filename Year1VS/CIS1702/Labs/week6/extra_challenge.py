# A program to validate students have the required prerequisites for enrolment of a requested module

def main():
    # Basic unit tests for can_enroll function
    run_tests()

    # Experimenting with a new student and the can_enroll function
    print("-- Enrolling new student --")
    students['s54321'] = []
    enrol_student('s54321', 'CIS1702')
    enrol_student('s54321', 'CIS2000') # Fails due to CIS1000 requirement
    enrol_student('s54321', 'CIS1000')
    enrol_student('s54321', 'CIS2000') # Succeeds due to updated modules

# Modules codes and their required prerequisites
modules = {
    'CIS1702': [],
    'CIS1000': ['CIS1702'],
    'CIS1001': ['CIS1702'],
    'CIS2000': ['CIS1000', 'CIS1702'],
    'MTH1001': [],
    'CIS2005': ['CIS1000', 'MTH1001']
}

# Students' IDs and their completed modules
students = {
    's12345': ['CIS1702', 'MTH1001'],
    's67890': ['CIS1702', 'CIS1001'],
    's54321': ['MTH1001']
}

# Adds the requested module to the student's record, if the student is able to enrol
def enrol_student(student_id, module_code):
    print(f"Attempting to enrol student {student_id} on module {module_code}...")
    if can_enrol(student_id, module_code):
        students[student_id].append(module_code)
        print("> Enrolment succeeded")
    else:
        print("> Enrolment failed")
    print()

# Verifies the student ID and module code are in the system, and returns True if the student has the required prerequisites, else False
def can_enrol(student_id, module_code):
    if not student_id in students:
        print("Student not found")
        return False 

    if not module_code in modules:
        print("Module not found")
        return False 
    
    completed_modules, required_modules = set(students[student_id]), set(modules[module_code])

    if module_code in completed_modules:
        print(f"Student is already enrolled in module {module_code}")
        return False 
    
    for module in required_modules:
        if module not in completed_modules:
            print(f"! Missing module {module} !")
            return False 
        
    return True 

'''
Unit tests for initial enrolment, and enrolment after aquiring needed prerequisites
Includes tests that are intended to fail, so will print to screen without returning
'''
def run_tests():
    print("-- Unit Tests --")
    # --- Unit Test 1---
    print("Running tests 1...")
    try:
        assert can_enrol("s12345", "CIS1000") == True
        assert can_enrol("s12345", "CIS2005") == True 
        assert can_enrol("s54321", "CIS1000") == False
    except AssertionError:
        print("> Tests 1 completed")
    print()

    # --- Unit Test 2---
    print("Running tests 2...")
    try:
        assert can_enrol('s54321', 'CIS1000') == False
        assert can_enrol('s12345', 'CIS1000') == True 

        print(f"Updated mododules: {students['s12345']}")

        assert can_enrol('s12345', 'CIS1000') == False 
        assert can_enrol('s12345', 'CIS2000') == True  
    except AssertionError:
        print("> Tests 2 completed")
    print()

main()