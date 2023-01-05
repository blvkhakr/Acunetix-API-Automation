import issues
import discovery

opt_list = ['1', '2' , '0']
bu_dict = {'a': 'business_unit_1', 'b':'business_unit_2', 'cp':'business_unit_3' } # ADD BU OPTIONS HERE
rp_list = ['m', 'M', 'd', 'D', 'exit']
ans_list = ['Yes', 'No']

try:
    user_input = input("Welcome to the Acunetix API Script.\n What would you like to do? Discovery [1], Metrics [2], exit [0]: ")
    while user_input != '0':
        if user_input not in opt_list:
            user_input = input("That's not an option. Your options are Discovery [1], Metrics [2], exit [0]: ")

        elif user_input == '1':
            discovery.pull_discovery()
            user_input = input("Want to do something else? Discovery [1], Metrics [2], exit [0]: ")

        elif user_input == "2":
            rp_answer = input("Do you want to run a report for a Manager ['M'], Developer ['D'], or Quit ['Q']: ")

            if rp_answer.upper() == 'Q':
                print("Exiting Metrics....")
                user_input = input("What would you like to do? Discovery [1], Metrics [2], exit [0]: ")
        
            elif rp_answer.upper() == 'M':
                unit = input("Which business unit? ['ADD BU OPTIONS HERE]: ") 
                if unit.lower() in bu_dict:
                    bu = bu_dict.get(unit)
                    issues.mgmt_rp(bu)
                    user_input = input("Want to do something else? Discovery [1], Metrics [2], exit [0]: ")
                else:
                    print("That's not an option")
        
            elif rp_answer.upper() == 'D':
                unit = input("Which business unit? ['ADD BU OPTIONS HERE]: ")
                if unit.lower() in bu_dict:
                    bu = bu_dict.get(unit)
                    issues.dev_rp(bu)
                    user_input = input("Want to do something else? Discovery [1], Metrics [2], exit [0]: ")
                else:
                    print("That's not an option")
            else:
                print("That's not an option")                     

except Exception:
    print("Something went wrong.")
finally:
    print("Til Next Time")
