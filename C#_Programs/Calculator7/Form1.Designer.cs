namespace Calculator7
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.num1 = new System.Windows.Forms.TextBox();
            this.num2 = new System.Windows.Forms.TextBox();
            this.modifier1 = new System.Windows.Forms.ComboBox();
            this.equal_sign_button = new System.Windows.Forms.Button();
            this.answer = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // num1
            // 
            this.num1.Location = new System.Drawing.Point(12, 94);
            this.num1.Name = "num1";
            this.num1.Size = new System.Drawing.Size(78, 20);
            this.num1.TabIndex = 0;
            this.num1.Text = "0";
            // 
            // num2
            // 
            this.num2.Location = new System.Drawing.Point(131, 94);
            this.num2.Name = "num2";
            this.num2.Size = new System.Drawing.Size(78, 20);
            this.num2.TabIndex = 1;
            this.num2.Text = "0";
            // 
            // modifier1
            // 
            this.modifier1.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.modifier1.FormattingEnabled = true;
            this.modifier1.ImeMode = System.Windows.Forms.ImeMode.NoControl;
            this.modifier1.Items.AddRange(new object[] {
            "+",
            "-",
            "/",
            "*"});
            this.modifier1.Location = new System.Drawing.Point(96, 94);
            this.modifier1.MaxDropDownItems = 4;
            this.modifier1.MaxLength = 1;
            this.modifier1.Name = "modifier1";
            this.modifier1.Size = new System.Drawing.Size(29, 21);
            this.modifier1.TabIndex = 2;
            // 
            // equal_sign_button
            // 
            this.equal_sign_button.Location = new System.Drawing.Point(215, 93);
            this.equal_sign_button.Name = "equal_sign_button";
            this.equal_sign_button.Size = new System.Drawing.Size(21, 23);
            this.equal_sign_button.TabIndex = 3;
            this.equal_sign_button.Text = "=";
            this.equal_sign_button.UseVisualStyleBackColor = true;
            this.equal_sign_button.Click += new System.EventHandler(this.equal_sign_button_Click);
            // 
            // answer
            // 
            this.answer.AutoSize = true;
            this.answer.BackColor = System.Drawing.SystemColors.Control;
            this.answer.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.answer.Location = new System.Drawing.Point(242, 97);
            this.answer.Name = "answer";
            this.answer.Size = new System.Drawing.Size(15, 15);
            this.answer.TabIndex = 4;
            this.answer.Text = "0";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(366, 360);
            this.Controls.Add(this.answer);
            this.Controls.Add(this.equal_sign_button);
            this.Controls.Add(this.modifier1);
            this.Controls.Add(this.num2);
            this.Controls.Add(this.num1);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedDialog;
            this.MaximizeBox = false;
            this.Name = "Form1";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Calculator Challenge";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox num1;
        private System.Windows.Forms.TextBox num2;
        private System.Windows.Forms.ComboBox modifier1;
        private System.Windows.Forms.Button equal_sign_button;
        private System.Windows.Forms.Label answer;
    }
}

