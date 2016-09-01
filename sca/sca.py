import lizard


filename = raw_input("Enter file location : ")

filetype = filename.split(".")[-1]


if filetype == "py" or filetype == "js" or filetype == "java":
    file_analysis = lizard.analyze_file(filename)
    # checkinf for presence of function
    if file_analysis.function_list == []:
        # if no function is present in the code
        print("-----Basic Analysis-----")
        for ele, value in file_analysis.__dict__.items():
            print(ele + "\t" + str(value))

    else:
        # if function are present in the code
        print("-----Functional Analysis-----")
        function_number = 1
        for func in file_analysis.function_list:
            print("---function number "+str(function_number)+"---")
            for ele, value in func.__dict__.items():
                print(ele+"\t"+str(value))
            function_number += 1



