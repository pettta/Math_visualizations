import os 
import sys 
import argparse
parser = argparse.ArgumentParser(description="Run manim command with optional test argument.")
parser.add_argument('--test', type=int, help='Specify a test number to run a specific command.')
args = parser.parse_args()

if args.test is not None:
    match args.test:
        case 1:
            print("Running Lorenz transform test.")
            command = "manim -pql chaos/lorenz.py OpenGLShow --renderer=opengl"
        case 2:
            print("Running 2x2 systems test with real positive eigenvalues of the same sign ")
            command = "manim -pql nxn_systems/2x2_systems.py RealEigenValuesPositiveSameSign --renderer=opengl"
        case 3:
            print("Running 2x2 systems test with real negative eigenvalues of the same sign ")
            command = "manim -pql nxn_systems/2x2_systems.py RealEigenValuesNegativeSameSign --renderer=opengl"
        case 4:
            print("Running 2x2 systems test with real eigenvalues of opposite sign ") 
            command = "manim -pql nxn_systems/2x2_systems.py RealEigenValuesOppositeSign --renderer=opengl" 
        case 5: 
            print("Running 2x2 systems test with complex eigenvalues (with nonzero real) ")
            command = "manim -pql nxn_systems/2x2_systems.py ComplexEigenValuesNonZeroRealPart --renderer=opengl"
        case 6: 
            print("Running 2x2 systems test with complex eigenvalues (with zero real) ")
            command = "manim -pql nxn_systems/2x2_systems.py ComplexEigenValuesZeroRealPart --renderer=opengl"
        case _:
            print("Test number not recognized.")
            sys.exit(1)
else:
    print("Please specify a test number.")
    sys.exit(1) 
    
os.system(command)
sys.exit(0)