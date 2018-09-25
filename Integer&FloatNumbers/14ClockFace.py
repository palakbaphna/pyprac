#H hours, M minutes and S seconds are passed since the midnight (0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60).
#  Determine the angle (in degrees) of the hour hand on the clock face right now.

H = int(input("H = ?"))

M = int(input("M = ?"))

S = int(input("S = ?"))

TotHours = round( (H + (M +(S/60))/60), 3)

print("Total number of hours are", TotHours)

if (0 <= H < 12)and (0<= M < 60) and (0<= S < 60):
    print("Total no. of hours, Hr = ", TotHours )
else:
    print("Invalid data")
    exit()

Angle = round( (30 * TotHours), 2)
print("Angle between hour hand and minute hand = ", Angle, "degrees")

