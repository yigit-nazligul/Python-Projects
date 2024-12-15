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
total_amount_of_medication_a = 0
total_amount_of_medication_b = 0



#Program Loop
while True:
    while True:
        TR_i_n = input("TR Identification Number:") 
        if len(TR_i_n) == 11 and TR_i_n.isdigit():
            break
        else:
            print("TR id must be a digit and must be 11 digits long !")
                  

    name_surname = input("Name and Surname:")

    dfpn = int(input("Deficient Factor Protein Number (8 or 9):"))

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



    antibody = int(input("Amount of Antibody in blood produced against factor medication (BU):"))

    #Is He/She will be included the Prophylaxis Programme ? 
    # 1 - Number of Antibody have to be 0
    # 2 - Severity of Hemophilia must be Mild
    # 3 - Number of bleeding episodes must be >= 36 

    nobe = int(input("Number of bleeding attacks in the past  year:"))

    if antibody == 0 and factor_level == "Severe" and nobe >= 36:
        is_applied = "Yes"
        weight_kg = int(input("Weight (kg):"))
        ptofm = input("the Production type of factor medication to be used (Plasma-derived/Recombinant(P/p/R/r))")
        total_prophylaxis += 1
        if dfpn == 8:
            total_iu_needed = weight_kg * (40-level) * 2
            total_amount_of_medication_a += total_iu_needed
            prophylaxis_A += 1
        elif dfpn == 9:
            prophylaxis_B += 1
            total_iu_needed = weight_kg * (40-level) 
            total_amount_of_medication_b += total_iu_needed

        

    else:
        is_applied = "No"

    print("TR identification number: {}\nName and Surname: {}\nType of the disease:{}\nSeverity of the disease:{}".format(TR_i_n,name_surname,dfpn,factor_level))
    if is_applied == "Yes":
        print("Prophylaxis will be applied !")

    else:
        print("Prophylaxis will not be applied !")

    if is_applied == "Yes":
            dose_2000 = 0
            dose_1500 = 0
            dose_1000 = 0
            dose_500 = 0
            dose_250 = 0

            remaining_medication = total_iu_needed

            # 2000 IU
            dose_2000 = remaining_medication // 2000
            remaining_medication = remaining_medication % 2000
            dose_2000+=1

            # 1500 IU
            dose_1500 = remaining_medication // 1500
            remaining_medication = remaining_medication % 1500
            dose_1500+=1

            # 1000 IU
            dose_1000 = remaining_medication // 1000
            remaining_medication = remaining_medication % 1000
            dose_1000+=1

            # 500 IU
            dose_500 = remaining_medication // 500
            remaining_medication = remaining_medication % 500
            dose_500+=1

            # 250 IU
            dose_250 = remaining_medication // 250
            remaining_medication = remaining_medication % 250
            dose_250+=1

            if ptofm == "r" or ptofm == "R":
                cost_1_time = float(total_iu_needed * 0.4)
            else:
                cost_1_time = float(total_iu_needed * 0.3)

            if dfpn == 8:
                weekly_cost = cost_1_time * 3
            else:
                weekly_cost = cost_1_time *2
            
            four_weekly_cost = weekly_cost * 4

            
            

            # Print Results
            print("Total required IU:", total_iu_needed, "IU")
            print("Doz dağılımı:")
            print("2000 IU: ", dose_2000)
            print("1500 IU: ", dose_1500)
            print("1000 IU: ", dose_1000)
            print("500 IU:  ", dose_500)
            print("250 IU:  ", dose_250)
            print("Cost for 1 use:",cost_1_time,"$")
            print("Cost for a week:", weekly_cost,"$")
            print("Cost for 4 weeks:",four_weekly_cost,"$")

                


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
print("Number of patients recieved prophylaxis with Factor 8:{}, Percentage:{}".format(prophylaxis_A,percentage_prophy_A))
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




        






