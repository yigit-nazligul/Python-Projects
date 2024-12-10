#Defining Variables
hem_a = 0
hem_b = 0
total_severe = 0
total_moderate = 0
total_mild = 0
total_patient = 0
total_recombinanted = 0
total_plasma = 0
total_prophylaxis = 0
prophylaxis_A = 0
prophylaxis_B = 0
amount_of_dose_A = 0
amount_of_dose_B = 0
total_vials = 0
total_cost = 0

#List to store patient details
patient = []

#Program Loop
while True:
    while True:
        TR_i_n = input("TR Identification Number:") 
        patient.append(TR_i_n)
        if len(TR_i_n) == 11 and TR_i_n.isdigit():
            break
        else:
            print("TR id must be a digit and must be 11 digits long !")
                  

    name_surname = input("Name and Surname:")
    patient.append(name_surname)

    dfpn = int(input("Deficient Factor Protein Number (8 or 9):"))
    patient.append(dfpn)
    if dfpn == 8:
        hem_a += 1
        total_patient += 1
            
    elif dfpn == 9:
        hem_b += 1
        total_patient += 1


    level = float(input("Factor Level in Blood (%):"))
    if level < 1 :
        factor_level = "Severe"
        total_severe += 1

    elif level >= 1 and level <= 5 :
        factor_level = "Moderate"
        total_moderate += 1

    elif level > 5 and level < 50:
        factor_level = "Mild"
        total_mild += 1
    patient.append(factor_level)


    antibody = int(input("Amount of Antibody in blood produced against factor medication (BU)"))
    patient.append(antibody)

    #Is He/She will be included the Prophylaxis Programme ? 
    # 1 - Number of Antibody have to be 0
    # 2 - Severity of Hemophilia must be Mild
    # 3 - Number of bleeding episodes must be >= 36 

    nobe = int(input("Number of bleeding attacks in the past  year:"))
    patient.append(nobe)

    if antibody == 0 and factor_level == "Severe" and nobe >= 36:
        is_applied = "Yes"
        total_prophylaxis += 1
        if dfpn == 8:
            prophylaxis_A += 1
        elif dfpn == 9:
            prophylaxis_B += 1

        weight_kg = int(input("Weight (kg):"))
        ptofm = input("the Production type of factor medication to be used (Plasma-derived/Recombinant(P/p/R/r))")
        patient.append(weight_kg)
        patient.append(ptofm)
    else:
        is_applied = "No"

    print("TR identification number: {}\nName and Surname: {}\nType of the disease:{}\nSeverity of the disease:{}".format(TR_i_n,name_surname,dfpn,factor_level))
    if is_applied == "Yes":
        print("Prophylaxis will be applied !")

    else:
        print("Prophylaxis will not be applied !")

    if is_applied == "Yes":
        if dfpn == 8 :
            weekly_usage = 3
            min_required_dose_iu_A = (40 - level) * weight_kg / 2
            amount_of_dose_A += min_required_dose_iu_A
            total_amount_of_medication_A = (40 - level) * weight_kg * 3 * 4
            vial_sizes = [2000,1500,1000,500] 
            vial_counts = [0,0,0,0] #Stores how many of each bottle size are needed
            i = 0 #Index to browse vial sizes
            remaining_medication = total_amount_of_medication #Choosing appropriate vials to accommodate the total amount of medication
            while remaining_medication > 0 and i < len(vial_sizes):
                # Calculate required number based on bottle size
                vial_counts[i] = remaining_medication // vial_sizes[i]
                # Update remaining medication amount
                remaining_medication %= vial_sizes[i]
                i += 1
                total_vials += vial_counts[i]

            if ptofm == "R" or ptofm == "r":
                cost = total_amount_of_medication * 0.4
                total_recombinanted +=1
                total_cost += cost

            elif ptofm == "P" or ptofm == "p":
                cost = total_amount_of_medication * 0.3
                total_plasma +=1
                total_cost += cost


            print("Factor {} and {} medication will be used".format(dfpn,ptofm))
            print("Need to use {} times a week the medication\nMinimum required dose of medication to be used at one time:{} IU".format(weekly_usage,total_amount_of_medication))
            print("Bottle sizes and numbers required:")
            for j in range(len(vial_sizes)):
                print(f"{vial_sizes[j]} ml bottle: {vial_counts[j]} quantity")

        elif dfpn == 9 :
            weekly_usage = 2
            min_required_dose_iu_B = (40 - level) * weight_kg
            total_amount_of_medication_B = (40 - level) * weight_kg * 2 * 4
            amount_of_dose_B += min_required_dose_iu_B
            vial_sizes = [2000,1500,1000,500] #
            vial_counts = [0,0,0,0] #Stores how many of each bottle size are needed
            i = 0 #Index to browse vial sizes
            remaining_medication = total_amount_of_medication #Choosing appropriate vials to accommodate the total amount of medication
            while remaining_medication > 0 and i < len(vial_sizes):
                # Calculate required number based on bottle size
                vial_counts[i] = remaining_medication // vial_sizes[i]
                # Update remaining medication amount
                remaining_medication %= vial_sizes[i]
                i += 1

            if ptofm == "R" or ptofm == "r":
                total_cost = total_amount_of_medication * 0.4
            elif ptofm == "P" or ptofm == "p":
                total_cost = total_amount_of_medication * 0.3


            print("Factor {} and {} medication will be used".format(dfpn,ptofm))
            print("Need to use {} times a week the medication\nMinimum required dose of medication to be used at one time:{} IU".format(weekly_usage,total_amount_of_medication))
            print("Bottle sizes and numbers required:")
            for j in range(len(vial_sizes)):
                print(f"{vial_sizes[j]} ml bottle: {vial_counts[j]} quantity")

        another = input("Is there any other patients ? (E/e/H/h)")
        if another == "E" or another == "e":
            continue
        else:
            break

#Displaying Summary
print("\nSummary:")
print("Total number of patients:", total_patient)
print("Number of patients with Factor 8:", hem_a)
print("Number of patients with Factor 9:", hem_b)
print("Number of patients with Severe Hemophilia:", total_severe)
percentage_severe = (total_severe / total_patient) * 100
print("Percent of patients with Severe Hemophilia:",percentage_severe)
print("Number of patients with Moderate Hemophilia:", total_moderate)
percentage_moderate = (total_moderate / total_patient) * 100
print("Percent of patients with moderate Hemophilia:", percentage_moderate)
print("Number of patients with Mild Hemophilia:", total_mild)
percentage_mild = (total_mild / total_patient) * 100
print("Percent of patients with mild Hemophilia:", percentage_mild)
percentage_prophy_A = (prophylaxis_A / total_prophylaxis) * 100
print("Number of patients recieved prophylaxis with Factor 8:{}, Percentage:{}".format(prophylaxis_A,percentage_prophy_B))
percentage_prophy_B = (prophylaxis_B / total_prophylaxis) * 100
print("Number of patients recieved prophylaxis with Factor 9:{}, Percentage:{}".format(prophylaxis_B,percentage_prophy_B))
print("Total number of patients with Prophylaxis applied:", total_prophylaxis)
total_iu = total_amount_of_medication_A + total_amount_of_medication_B
print("Total Amount (IU):",total_iu)
print("Total vials:",total_vials)
average_iu = total_iu / (prophylaxis_A + prophylaxis_B)
average_cost = total_cost / (prophylaxis_A + prophylaxis_B)
yearly_cost = total_cost * 12
print("Average annual total medication amount IU:{}, Cost:{} for the patients covered by SSI".format(average_iu,average_cost))
print("4 weekly Cost:{}, yearly cost:{}".format(total_cost,yearly_cost))




        






