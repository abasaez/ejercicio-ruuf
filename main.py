from typing import List, Tuple, Dict
import json

#Find the max amount of rectangular panels of dimensions a & b to fit a roof of dimensions x & y.


def calculate_panels(panel_width: int, panel_height: int, 
                    roof_width: int, roof_height: int) -> int:

    i = 0
    answers = [0] * 2

    while i < 2:
        placed_panels = 0
        #Place panels on the roof on a single orientation, calculate tiles placed and any remainder strips.
        if (panel_width <= roof_width) and (panel_height <= roof_height):
            remainder_width = roof_width % panel_width
            remainder_height = roof_height % panel_height
            placed_panels = ((roof_height-remainder_height)//panel_height) * ((roof_width-remainder_width)//panel_width)


        #Rotate the panels and try to fill the remainder strips
            if (panel_height <= remainder_width) and (panel_width <= roof_height):
                new_remainder_width = remainder_width % panel_height
                placed_panels += ((remainder_width- new_remainder_width)//panel_height) * (roof_height//panel_width)

            if (panel_width <= remainder_height) and (panel_height <= roof_width):
                new_remainder_height = remainder_height % panel_width
                placed_panels += (roof_width//panel_height) * ((remainder_height - new_remainder_height)//panel_width)

        #Do this starting with both orientations, and return the the maximum between both of them.
        answers[i] = placed_panels
        i += 1
        panel_width, panel_height = panel_height, panel_width

    ans = max(answers[0], answers[1])
    return ans

#Fits panels in a triangular roof by subdividing the triangle into a series of rectangles
def calculate_panels_triangle(panel_width: int, panel_height: int, 
                    roof_width: int, roof_height: int) -> int:

    print(f"\n Triangular Roof Calculation: ")
    print(f"Roof dimensions: {roof_width} x {roof_height} (area = {roof_width * roof_height//2})")
    print(f"Panel dimensions: {panel_width} x {panel_height} (area = {panel_width * panel_height})")

    i = 0
    answers = [0] * 2

    while i < 2:
        placed_panels= 0    
        current_height = 0

        #Divide the triangular area into rectangles of height = panel height, fit as many as possible, and repeat for every floor.
        while current_height + panel_height <= roof_height:
            current_width = int(roof_width * (1 - (current_height + panel_height) / roof_height))
            placed_panels += calculate_panels(panel_width, panel_height, current_width, panel_height)
            current_height += panel_height

        #Iterate using the panel width instead of the height, and pick the best answer
        answers[i] = placed_panels
        i += 1
        panel_width, panel_height = panel_height, panel_width

    ans = int(max(answers[0], answers[1]))
    print(f"Area covered: {ans * panel_height * panel_width}")
    print(f"{ans * panel_height * panel_width/(roof_width * roof_height//2)*100}%")
    return ans


def run_tests() -> None:
    with open('test_cases.json', 'r') as f:
        data = json.load(f)
        test_cases: List[Dict[str, int]] = [
            {
                "panel_w": test["panelW"],
                "panel_h": test["panelH"],
                "roof_w": test["roofW"],
                "roof_h": test["roofH"],
                "expected": test["expected"]
            }
            for test in data["testCases"]
        ]
    
    print("Corriendo tests:")
    print("-------------------")
    
    for i, test in enumerate(test_cases, 1):
        result = calculate_panels(
            test["panel_w"], test["panel_h"], 
            test["roof_w"], test["roof_h"]
        )
        passed = result == test["expected"]
        
        print(f"Test {i}:")
        print(f"  Panels: {test['panel_w']}x{test['panel_h']}, "
              f"Roof: {test['roof_w']}x{test['roof_h']}")
        print(f"  Expected: {test['expected']}, Got: {result}")
        print(f"  Status: {'✅ PASSED' if passed else '❌ FAILED'}\n")


triangle_tests = [
    (7, 10, 100, 100),
    (5, 5, 120, 80),
    (4, 3, 90, 60),
    (10, 5, 150, 100),
    (6, 4, 80, 60),
    (9, 9, 150, 120),
    (12, 8, 200, 100),
    (15, 5, 180, 100),
    (4, 4, 20, 20),
    (15, 15, 50, 50),
    (25, 10, 60, 40),
    (50, 50, 100, 80),
    (90, 20, 100, 50)
]


def main() -> None:
    print("🐕 Wuuf wuuf wuuf 🐕")
    print("================================\n")
    
    run_tests()


    for i, (pw, ph, rw, rh) in enumerate(triangle_tests, 1):
        print(f"\n[Triangle Test {i}] Panels: {pw}x{ph}, Roof: {rw}x{rh}")
        print("Placed panels: ",calculate_panels_triangle(pw, ph, rw, rh))

if __name__ == "__main__":
    main()
