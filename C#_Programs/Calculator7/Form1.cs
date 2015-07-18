using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Calculator7
{
    public partial class Form1 : Form
    {   
        public Form1()
        {
            InitializeComponent();
        }
        
        private void Form1_Load(object sender, EventArgs e)
        {
            // This serves no purpose from what I can tell and I have not found a way to comfortably delete it yet. (Best to be safe on the safe side!)
        }

        private void equal_sign_button_Click(object sender, EventArgs e)
        {
            double number1, number2, ans; // Identify variables as double to account for decimals.
            string symbol = modifier1.Text; // Read the selected modifier symbol to use for calculations.
            ans = 0.0;
            string num1_text = Convert.ToString(num1.Text); // Convert to string initially to check for non-numerical input.
            string num2_text = Convert.ToString(num2.Text);
            bool isNum1Good = double.TryParse(num1_text, out number1); // Return false if not numerical input.
            bool isNum2Good = double.TryParse(num2_text, out number2);

            if (isNum1Good == false || isNum2Good == false) { answer.Text = "Invalid input."; return; } // Catch non-numerical input.
            if (symbol == "/" && number2 == 0) { answer.Text = "Invalid input."; return; } // Catch divide by zero errors.

            number1 = Convert.ToDouble(num1.Text); // Convert the contents of the textBox into a double.
            number2 = Convert.ToDouble(num2.Text); 

            switch(symbol) // Selects appropriate action based on the modification symbol.
            {
               case "+": ans = number1 + number2; break;
               case "-": ans = number1 - number2; break;
               case "*": ans = number1 * number2; break;
               case "/": ans = number1 / number2; break;
               default : answer.Text = "Invalid sign."; return;
            }   
            answer.Text = ans.ToString("n"); // Change label value (the answer) to a number.
        }
    }
}
