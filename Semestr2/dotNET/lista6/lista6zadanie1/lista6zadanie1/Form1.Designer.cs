namespace lista6zadanie1
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
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
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            groupBox1 = new GroupBox();
            label2 = new Label();
            label1 = new Label();
            textBox2 = new TextBox();
            textBox1 = new TextBox();
            groupBox2 = new GroupBox();
            checkBox2 = new CheckBox();
            checkBox1 = new CheckBox();
            comboBox1 = new ComboBox();
            label3 = new Label();
            button1 = new Button();
            btnAccept = new Button();
            groupBox1.SuspendLayout();
            groupBox2.SuspendLayout();
            SuspendLayout();
            // 
            // groupBox1
            // 
            groupBox1.Anchor = AnchorStyles.Top | AnchorStyles.Left | AnchorStyles.Right;
            groupBox1.Controls.Add(label2);
            groupBox1.Controls.Add(label1);
            groupBox1.Controls.Add(textBox2);
            groupBox1.Controls.Add(textBox1);
            groupBox1.Location = new Point(16, 15);
            groupBox1.Margin = new Padding(200);
            groupBox1.Name = "groupBox1";
            groupBox1.Size = new Size(766, 169);
            groupBox1.TabIndex = 0;
            groupBox1.TabStop = false;
            groupBox1.Text = "Uczelnia";
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(20, 87);
            label2.Name = "label2";
            label2.Size = new Size(40, 15);
            label2.TabIndex = 3;
            label2.Text = "Adres:";
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(20, 45);
            label1.Name = "label1";
            label1.Size = new Size(45, 15);
            label1.TabIndex = 2;
            label1.Text = "Nazwa:";
            // 
            // textBox2
            // 
            textBox2.Location = new Point(117, 84);
            textBox2.Name = "textBox2";
            textBox2.Size = new Size(629, 23);
            textBox2.TabIndex = 1;
            textBox2.TextChanged += textBox2_TextChanged;
            // 
            // textBox1
            // 
            textBox1.Location = new Point(117, 42);
            textBox1.Name = "textBox1";
            textBox1.Size = new Size(629, 23);
            textBox1.TabIndex = 0;
            textBox1.TextChanged += textBox1_TextChanged;
            // 
            // groupBox2
            // 
            groupBox2.Controls.Add(checkBox2);
            groupBox2.Controls.Add(checkBox1);
            groupBox2.Controls.Add(comboBox1);
            groupBox2.Controls.Add(label3);
            groupBox2.Location = new Point(16, 196);
            groupBox2.Name = "groupBox2";
            groupBox2.Size = new Size(766, 198);
            groupBox2.TabIndex = 1;
            groupBox2.TabStop = false;
            groupBox2.Text = "Rodzaj studiow";
            // 
            // checkBox2
            // 
            checkBox2.AutoSize = true;
            checkBox2.Location = new Point(266, 138);
            checkBox2.Name = "checkBox2";
            checkBox2.Size = new Size(98, 19);
            checkBox2.TabIndex = 3;
            checkBox2.Text = "uzupelniajace";
            checkBox2.UseVisualStyleBackColor = true;
            checkBox2.CheckedChanged += checkBox2_CheckedChanged;
            // 
            // checkBox1
            // 
            checkBox1.AutoSize = true;
            checkBox1.Location = new Point(143, 138);
            checkBox1.Name = "checkBox1";
            checkBox1.Size = new Size(67, 19);
            checkBox1.TabIndex = 2;
            checkBox1.Text = "dzienne";
            checkBox1.UseVisualStyleBackColor = true;
            checkBox1.CheckedChanged += checkBox1_CheckedChanged;
            // 
            // comboBox1
            // 
            comboBox1.DropDownStyle = ComboBoxStyle.DropDownList;
            comboBox1.FormattingEnabled = true;
            comboBox1.Items.AddRange(new object[] { "3 letnie", "3,5 letnie" });
            comboBox1.Location = new Point(122, 71);
            comboBox1.Name = "comboBox1";
            comboBox1.Size = new Size(589, 23);
            comboBox1.TabIndex = 1;
            comboBox1.SelectedIndexChanged += comboBox1_SelectedIndexChanged;
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Location = new Point(20, 74);
            label3.Name = "label3";
            label3.Size = new Size(65, 15);
            label3.TabIndex = 0;
            label3.Text = "Cykl nauki:";
            // 
            // button1
            // 
            button1.Location = new Point(582, 400);
            button1.Name = "button1";
            button1.Size = new Size(200, 40);
            button1.TabIndex = 2;
            button1.Text = "Anuluj";
            button1.UseVisualStyleBackColor = true;
            button1.Click += button1_Click;
            // 
            // btnAccept
            // 
            btnAccept.Location = new Point(16, 400);
            btnAccept.Name = "btnAccept";
            btnAccept.Size = new Size(200, 40);
            btnAccept.TabIndex = 3;
            btnAccept.Text = "Akceptuj";
            btnAccept.UseVisualStyleBackColor = true;
            btnAccept.Click += btnAccept_Click;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(btnAccept);
            Controls.Add(button1);
            Controls.Add(groupBox2);
            Controls.Add(groupBox1);
            Name = "Form1";
            Text = "Wybor uczelni";
            groupBox1.ResumeLayout(false);
            groupBox1.PerformLayout();
            groupBox2.ResumeLayout(false);
            groupBox2.PerformLayout();
            ResumeLayout(false);
        }

        #endregion

        private GroupBox groupBox1;
        private GroupBox groupBox2;
        private Button button1;
        private Button btnAccept;
        private TextBox textBox2;
        private TextBox textBox1;
        private Label label2;
        private Label label1;
        private ComboBox comboBox1;
        private Label label3;
        private CheckBox checkBox2;
        private CheckBox checkBox1;
    }
}