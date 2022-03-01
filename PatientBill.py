
import PatientClass as pc
import ProcedureClass as pr

pat = pc.Patient(1, "Matt Jones", "123 Main st, Waco TX 76706", "254-555-7415", "TRUE")

proc1 = pr.Procedure("Physical Exam", "2/15/2022", "Dr. Irvine", 250, 1)
proc2 = pr.Procedure("MRI", "2/15/2022", "Dr. Hamilton", 1500, 1)
proc3 = pr.Procedure("CT Scan", "2/17/2022", "Dr. Drey", 1200, 2)

print("*** Patient Bill ***")
print("Name: ", pat.get_name())
print("Address: ", pat.get_add())
print("Phone: ", pat.get_phone())
print()

tot_charge = 0

if pat.get_ID() == proc1.get_pinfo():
    print("Procedure: ", proc1.get_nop())
    print("Date: ", proc1.get_dop())
    print("Practitioner: ", proc1.get_prac())
    print("Charge: $", float(proc1.get_charge()))
    print()
    tot_charge += float(proc1.get_charge())
if pat.get_ID() == proc2.get_pinfo():
    print("Procedure: ", proc2.get_nop())
    print("Date: ", proc2.get_dop())
    print("Practitioner: ", proc2.get_prac())
    print("Charge: $", float(proc2.get_charge()))
    print()
    tot_charge += float(proc2.get_charge())
if pat.get_ID() == proc3.get_pinfo():
    print("Procedure: ", proc3.get_nop())
    print("Date: ", proc3.get_dop())
    print("Practitioner: ", proc3.get_prac())
    print("Charge: $", float(proc3.get_charge()))
    print()
    tot_charge += float(proc3.get_charge())
if pat.get_vs() == "TRUE":
    tot_charge = tot_charge - (0.40 * tot_charge)
    print("Total Charges: ","${:,.2f}".format(tot_charge))
else:
    print("Total Charges: ","${:,.2f}".format(tot_charge))

print()