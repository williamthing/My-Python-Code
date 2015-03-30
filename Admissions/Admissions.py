#!/usr/bin/python
# William Thing
# April 20, 2014
# Admissions
#
# This program will compare two different applicants
# taking in either their ACT or SAT score and overall
# GPA to determine which applicant is more competitive.


# Prints the introduction of the Admissions program
def intro_to_program():
   print("This program compares two applicants to"); 
   print("determine which one seems like the stronger"); 
   print("applicant. For each candidate I will need");
   print("either SAT or ACT scores plus a weighted GPA.");
   print("");
   
# Ask the user if they want to either enter a student's SAT or ACT score
# and returns their overall score for comparison of competitiveness.
def use_ACT_or_SAT():
   response = raw_input("do you have 1) SAT scores or 2) ACT scores? ");
   if (response == '1'):
      return calc_SAT();
   else:
      return calc_ACT();
   
# Returns an overall score from user's ACT score input.
# Also prints student's exam score and gpa score.
def calc_ACT():
   ACT_english_score = int(raw_input("ACT English? "));
   ACT_math_score = int(raw_input("ACT math? "));
   ACT_reading_score = int(raw_input("ACT reading? "));
   ACT_science_score = int(raw_input("ACT science? "));
   exam_score = (ACT_english_score + 2*ACT_math_score + 
            ACT_reading_score + ACT_science_score)/1.8;
   print("exam score = %.1f" % exam_score);
   gpa_score = gpa_score_calc();
   return exam_score + gpa_score;
   
# Returns an overall score from user's SAT score input.
# Also prints student's exam score and gpa score.
def calc_SAT():
   SAT_math_score = int(raw_input("SAT math? "));
   SAT_reading_score = int(raw_input("SAT critical reading? "));
   SAT_writing_score = int(raw_input("SAT writing? "));
   exam_score = float((2 * SAT_math_score + SAT_reading_score
                                    + SAT_writing_score)/32);
   print("exam score = %.1f" % exam_score);
   gpa_score = gpa_score_calc();
   return exam_score + gpa_score;
   
# Returns overall gpa score determined by users gpa inputs   
def gpa_score_calc():
   gpa = float(raw_input("overall GPA? "));
   max_gpa = float(raw_input("max GPA? "));
   trans_mult = float(raw_input("Transcript Multiplier? "));
   gpa_score = gpa/max_gpa * 100 * trans_mult;
   print("GPA score = %.1f" % gpa_score);
   return gpa_score;
      
# Takes in two applicant's score for comparison and prints outcome
def admissions_decision(app_one, app_two):
   if (app_one > app_two):
      print("The first applicant seems to be better");
   elif (app_two > app_one):
      print("The second applicant seems to be better");
   else:
      print("Hard decision both applicant have same scores");  
   
   
def main():
   intro_to_program();
   print("Information for applicant #1:");
   app_one_score = use_ACT_or_SAT();
   print("");
   print("Information for applicant #2:");
   app_two_score = use_ACT_or_SAT();
   print("");
   print("First applicant overall score   = %.1f" % app_one_score);
   print("Second applicant overall score  = %.1f" % app_two_score);
   admissions_decision(app_one_score, app_two_score);
   
if __name__ == "__main__": main();
