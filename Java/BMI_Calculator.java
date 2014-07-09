import java.util.Scanner;

public class BMI_Calculator
{
	private static Scanner userInput;

	// BMI formula:
	// BMI = pounds x 4.88 / (height*height)
	public static void main(String[]args)
	{
		userInput = new Scanner(System.in);
		double pounds, feet, inches, height, BMI;
		
		System.out.println("-- BMI Calculator --");
		System.out.println("Please note: This is calculator does not take into effect" +
				"\nage, gender, and several other factors. It is merely meant to give an approximation.\n");
		System.out.println("Please enter your height in feet followed by inches.");
		
		System.out.println("Feet: ");
		feet = userInput.nextDouble();		
		System.out.println("Inches: ");
		inches = userInput.nextDouble();
		System.out.println("Please enter your weight now, in pounds: ");
		pounds = userInput.nextDouble();
		
		height = (feet + (inches / 12));
		BMI = (pounds * 4.88 / (height*height));
		System.out.println("Your BMI is: " + BMI);
		
		String classify = "Your BMI classisfies you as ";
		
		if(BMI < 16.0) {
			System.out.println(classify + "severly underweight. Please seek help.");
		} else if(BMI > 16.0 && BMI < 18.5) {
			System.out.println(classify + "underweight. You may want to seek help.");
		} else if(BMI > 18.5 && BMI < 24.9) {
			System.out.println(classify + "normal weight. Keep up the healthy weight!");
		} else if(BMI > 24.9 && BMI < 29.9) {
			System.out.println(classify + "overweight. You may want to seek help.");
		} else if(BMI > 30) {
			System.out.println(classify + "obese. Please seek help.");
		} else {
			System.out.println("System error. Please restart the program and try again.");
		}
	}
}
