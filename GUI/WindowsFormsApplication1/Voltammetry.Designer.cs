namespace WindowsFormsApplication1
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
            System.Windows.Forms.DataVisualization.Charting.ChartArea chartArea1 = new System.Windows.Forms.DataVisualization.Charting.ChartArea();
            System.Windows.Forms.DataVisualization.Charting.Legend legend1 = new System.Windows.Forms.DataVisualization.Charting.Legend();
            System.Windows.Forms.DataVisualization.Charting.Series series1 = new System.Windows.Forms.DataVisualization.Charting.Series();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.ScanBox = new System.Windows.Forms.TextBox();
            this.label6 = new System.Windows.Forms.Label();
            this.SampleBox = new System.Windows.Forms.TextBox();
            this.label8 = new System.Windows.Forms.Label();
            this.SensitivityBox = new System.Windows.Forms.TextBox();
            this.label9 = new System.Windows.Forms.Label();
            this.ButtonStart = new System.Windows.Forms.Button();
            this.PortBox = new System.Windows.Forms.TextBox();
            this.label5 = new System.Windows.Forms.Label();
            this.HostBox = new System.Windows.Forms.TextBox();
            this.label7 = new System.Windows.Forms.Label();
            this.ButtonScan = new System.Windows.Forms.Button();
            this.ButtonConnect = new System.Windows.Forms.Button();
            this.ButtonDisconnect = new System.Windows.Forms.Button();
            this.StatusBox = new System.Windows.Forms.TextBox();
            this.InitE = new System.Windows.Forms.NumericUpDown();
            this.HighE = new System.Windows.Forms.NumericUpDown();
            this.LowE = new System.Windows.Forms.NumericUpDown();
            this.FinalE = new System.Windows.Forms.NumericUpDown();
            this.VoltGraph = new System.Windows.Forms.DataVisualization.Charting.Chart();
            this.Refresh_Graph = new System.Windows.Forms.Button();
            this.Clear_Graph = new System.Windows.Forms.Button();
            this.Load_Data = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.InitE)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.HighE)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.LowE)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.FinalE)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.VoltGraph)).BeginInit();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 9);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(47, 13);
            this.label1.TabIndex = 0;
            this.label1.Text = "Init E [V]";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(12, 35);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(55, 13);
            this.label2.TabIndex = 2;
            this.label2.Text = "High E [V]";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(12, 61);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(53, 13);
            this.label3.TabIndex = 4;
            this.label3.Text = "Low E [V]";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(12, 87);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(55, 13);
            this.label4.TabIndex = 6;
            this.label4.Text = "Final E [V]";
            // 
            // ScanBox
            // 
            this.ScanBox.Location = new System.Drawing.Point(113, 106);
            this.ScanBox.Name = "ScanBox";
            this.ScanBox.Size = new System.Drawing.Size(100, 20);
            this.ScanBox.TabIndex = 11;
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(12, 113);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(84, 13);
            this.label6.TabIndex = 10;
            this.label6.Text = "Scan Rate [V/s]";
            // 
            // SampleBox
            // 
            this.SampleBox.Location = new System.Drawing.Point(113, 132);
            this.SampleBox.Name = "SampleBox";
            this.SampleBox.Size = new System.Drawing.Size(100, 20);
            this.SampleBox.TabIndex = 15;
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Location = new System.Drawing.Point(12, 139);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(96, 13);
            this.label8.TabIndex = 14;
            this.label8.Text = "Sample Interval [V]";
            // 
            // SensitivityBox
            // 
            this.SensitivityBox.Location = new System.Drawing.Point(113, 158);
            this.SensitivityBox.Name = "SensitivityBox";
            this.SensitivityBox.Size = new System.Drawing.Size(100, 20);
            this.SensitivityBox.TabIndex = 17;
            // 
            // label9
            // 
            this.label9.AutoSize = true;
            this.label9.Location = new System.Drawing.Point(12, 165);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(82, 13);
            this.label9.TabIndex = 16;
            this.label9.Text = "Sensitivity [A/V]";
            // 
            // ButtonStart
            // 
            this.ButtonStart.Location = new System.Drawing.Point(15, 193);
            this.ButtonStart.Name = "ButtonStart";
            this.ButtonStart.Size = new System.Drawing.Size(75, 23);
            this.ButtonStart.TabIndex = 18;
            this.ButtonStart.Text = "Start";
            this.ButtonStart.UseVisualStyleBackColor = true;
            this.ButtonStart.Click += new System.EventHandler(this.StartButton_Click);
            // 
            // PortBox
            // 
            this.PortBox.Location = new System.Drawing.Point(346, 28);
            this.PortBox.Name = "PortBox";
            this.PortBox.Size = new System.Drawing.Size(100, 20);
            this.PortBox.TabIndex = 22;
            this.PortBox.Text = "50525";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(247, 35);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(36, 13);
            this.label5.TabIndex = 21;
            this.label5.Text = "Port #";
            // 
            // HostBox
            // 
            this.HostBox.Location = new System.Drawing.Point(346, 2);
            this.HostBox.Name = "HostBox";
            this.HostBox.Size = new System.Drawing.Size(100, 20);
            this.HostBox.TabIndex = 20;
            this.HostBox.Text = "192.168.137.73";
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(247, 9);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(83, 13);
            this.label7.TabIndex = 19;
            this.label7.Text = "Host IP Address";
            // 
            // ButtonScan
            // 
            this.ButtonScan.Location = new System.Drawing.Point(250, 77);
            this.ButtonScan.Name = "ButtonScan";
            this.ButtonScan.Size = new System.Drawing.Size(75, 23);
            this.ButtonScan.TabIndex = 23;
            this.ButtonScan.Text = "Scan IPs?";
            this.ButtonScan.UseVisualStyleBackColor = true;
            // 
            // ButtonConnect
            // 
            this.ButtonConnect.Location = new System.Drawing.Point(346, 77);
            this.ButtonConnect.Name = "ButtonConnect";
            this.ButtonConnect.Size = new System.Drawing.Size(75, 23);
            this.ButtonConnect.TabIndex = 24;
            this.ButtonConnect.Text = "Connect";
            this.ButtonConnect.UseVisualStyleBackColor = true;
            this.ButtonConnect.Click += new System.EventHandler(this.ConnectButton_Click);
            // 
            // ButtonDisconnect
            // 
            this.ButtonDisconnect.Location = new System.Drawing.Point(427, 77);
            this.ButtonDisconnect.Name = "ButtonDisconnect";
            this.ButtonDisconnect.Size = new System.Drawing.Size(75, 23);
            this.ButtonDisconnect.TabIndex = 25;
            this.ButtonDisconnect.Text = "Disconnect";
            this.ButtonDisconnect.UseVisualStyleBackColor = true;
            this.ButtonDisconnect.Click += new System.EventHandler(this.DisconnectButton_Click);
            // 
            // StatusBox
            // 
            this.StatusBox.Location = new System.Drawing.Point(250, 122);
            this.StatusBox.Multiline = true;
            this.StatusBox.Name = "StatusBox";
            this.StatusBox.Size = new System.Drawing.Size(229, 81);
            this.StatusBox.TabIndex = 26;
            // 
            // InitE
            // 
            this.InitE.DecimalPlaces = 3;
            this.InitE.Increment = new decimal(new int[] {
            1,
            0,
            0,
            131072});
            this.InitE.Location = new System.Drawing.Point(113, 2);
            this.InitE.Maximum = new decimal(new int[] {
            4,
            0,
            0,
            65536});
            this.InitE.Name = "InitE";
            this.InitE.Size = new System.Drawing.Size(65, 20);
            this.InitE.TabIndex = 27;
            this.InitE.Value = new decimal(new int[] {
            10,
            0,
            0,
            196608});
            // 
            // HighE
            // 
            this.HighE.DecimalPlaces = 3;
            this.HighE.Increment = new decimal(new int[] {
            1,
            0,
            0,
            131072});
            this.HighE.Location = new System.Drawing.Point(113, 28);
            this.HighE.Maximum = new decimal(new int[] {
            4,
            0,
            0,
            65536});
            this.HighE.Name = "HighE";
            this.HighE.Size = new System.Drawing.Size(65, 20);
            this.HighE.TabIndex = 28;
            this.HighE.Value = new decimal(new int[] {
            40,
            0,
            0,
            131072});
            // 
            // LowE
            // 
            this.LowE.DecimalPlaces = 3;
            this.LowE.Increment = new decimal(new int[] {
            1,
            0,
            0,
            196608});
            this.LowE.Location = new System.Drawing.Point(113, 54);
            this.LowE.Maximum = new decimal(new int[] {
            4,
            0,
            0,
            65536});
            this.LowE.Name = "LowE";
            this.LowE.Size = new System.Drawing.Size(65, 20);
            this.LowE.TabIndex = 29;
            // 
            // FinalE
            // 
            this.FinalE.DecimalPlaces = 3;
            this.FinalE.Increment = new decimal(new int[] {
            1,
            0,
            0,
            196608});
            this.FinalE.Location = new System.Drawing.Point(113, 80);
            this.FinalE.Maximum = new decimal(new int[] {
            4,
            0,
            0,
            65536});
            this.FinalE.Name = "FinalE";
            this.FinalE.Size = new System.Drawing.Size(65, 20);
            this.FinalE.TabIndex = 30;
            // 
            // VoltGraph
            // 
            chartArea1.Name = "ChartArea1";
            this.VoltGraph.ChartAreas.Add(chartArea1);
            legend1.Name = "Legend1";
            this.VoltGraph.Legends.Add(legend1);
            this.VoltGraph.Location = new System.Drawing.Point(508, 9);
            this.VoltGraph.Name = "VoltGraph";
            series1.ChartArea = "ChartArea1";
            series1.ChartType = System.Windows.Forms.DataVisualization.Charting.SeriesChartType.Line;
            series1.Legend = "Legend1";
            series1.Name = "Series1";
            this.VoltGraph.Series.Add(series1);
            this.VoltGraph.Size = new System.Drawing.Size(452, 300);
            this.VoltGraph.TabIndex = 31;
            this.VoltGraph.Text = "VoltGraph";
            // 
            // Refresh_Graph
            // 
            this.Refresh_Graph.Location = new System.Drawing.Point(403, 257);
            this.Refresh_Graph.Name = "Refresh_Graph";
            this.Refresh_Graph.Size = new System.Drawing.Size(99, 23);
            this.Refresh_Graph.TabIndex = 32;
            this.Refresh_Graph.Text = "Refresh_Graph";
            this.Refresh_Graph.UseVisualStyleBackColor = true;
            this.Refresh_Graph.Click += new System.EventHandler(this.Refresh_Graph_Click);
            // 
            // Clear_Graph
            // 
            this.Clear_Graph.Location = new System.Drawing.Point(403, 286);
            this.Clear_Graph.Name = "Clear_Graph";
            this.Clear_Graph.Size = new System.Drawing.Size(99, 23);
            this.Clear_Graph.TabIndex = 33;
            this.Clear_Graph.Text = "Clear_Graph";
            this.Clear_Graph.UseVisualStyleBackColor = true;
            this.Clear_Graph.Click += new System.EventHandler(this.Clear_Graph_Click);
            // 
            // Load_Data
            // 
            this.Load_Data.Location = new System.Drawing.Point(403, 228);
            this.Load_Data.Name = "Load_Data";
            this.Load_Data.Size = new System.Drawing.Size(99, 23);
            this.Load_Data.TabIndex = 34;
            this.Load_Data.Text = "Load_Data";
            this.Load_Data.UseVisualStyleBackColor = true;
            this.Load_Data.Click += new System.EventHandler(this.Load_Data_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(965, 322);
            this.Controls.Add(this.Load_Data);
            this.Controls.Add(this.Clear_Graph);
            this.Controls.Add(this.Refresh_Graph);
            this.Controls.Add(this.VoltGraph);
            this.Controls.Add(this.FinalE);
            this.Controls.Add(this.LowE);
            this.Controls.Add(this.HighE);
            this.Controls.Add(this.InitE);
            this.Controls.Add(this.StatusBox);
            this.Controls.Add(this.ButtonDisconnect);
            this.Controls.Add(this.ButtonConnect);
            this.Controls.Add(this.ButtonScan);
            this.Controls.Add(this.PortBox);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.HostBox);
            this.Controls.Add(this.label7);
            this.Controls.Add(this.ButtonStart);
            this.Controls.Add(this.SensitivityBox);
            this.Controls.Add(this.label9);
            this.Controls.Add(this.SampleBox);
            this.Controls.Add(this.label8);
            this.Controls.Add(this.ScanBox);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "Client";
            ((System.ComponentModel.ISupportInitialize)(this.InitE)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.HighE)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.LowE)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.FinalE)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.VoltGraph)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.TextBox ScanBox;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.TextBox SampleBox;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.TextBox SensitivityBox;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.Button ButtonStart;
        private System.Windows.Forms.TextBox PortBox;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.TextBox HostBox;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.Button ButtonScan;
        private System.Windows.Forms.Button ButtonConnect;
        private System.Windows.Forms.Button ButtonDisconnect;
        private System.Windows.Forms.TextBox StatusBox;
        private System.Windows.Forms.NumericUpDown InitE;
        private System.Windows.Forms.NumericUpDown HighE;
        private System.Windows.Forms.NumericUpDown LowE;
        private System.Windows.Forms.NumericUpDown FinalE;
        private System.Windows.Forms.DataVisualization.Charting.Chart VoltGraph;
        private System.Windows.Forms.Button Refresh_Graph;
        private System.Windows.Forms.Button Clear_Graph;
        private System.Windows.Forms.Button Load_Data;
    }
}

