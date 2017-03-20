//using SimpleTCP;
using System;
using System.Windows.Forms;
using System.Net;
using System.Net.Sockets;
using System.Threading;
using System.Text;
using System.Data;
using System.Data.OleDb;
using System.Globalization;
using System.IO;
using System.Collections.Generic;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void StartButton_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Initiating Test Sequence");
            //send data over TCP/IP socket
            //send user inputs

            //run pwm.py with inputs
            //save onboard in CSV
            //receive CSV on laptop
            //transform to graph
        }

        private void ConnectButton_Click(object sender, EventArgs e)
        {
            int flag = 1;
            decimal input0 = InitE.Value;
            decimal input1 = HighE.Value;
            decimal input2 = LowE.Value;
            decimal input3 = FinalE.Value;
            flag = AsynchronousClient.StartClient(input0, input1, input2, input3);

            //run client.py equivalent here in C#
            //possible functionality
            //scan for IP addresses the Pi may be assigned to in order to better automate the connection process
            //check if connection has been established, set flag to 1 if successful

            //int flag = 1;
            if (flag == 0)
            {
                MessageBox.Show("Connecting to Host");
            }
            else
            {
                MessageBox.Show("Connection error...");
            }
        }

        private void DisconnectButton_Click(object sender, EventArgs e)
        {
            //send a CTRL+C command to kill client.py

            //Socket client = existing socket;
            //client.Shutdown(SocketShutdown.Both);
            //client.Close();

        }

        private void Load_Data_Click(object sender, EventArgs e)
        {
            //string filepath = "C:\\Users\\Brutalocalypse\\Desktop\\adc_test_1.csv";
            //System.Data.DataTable dtab = ConvertCSVtoDataTable(filepath);

            // chart = GetDataTableFromCsv();
            //GetDataTableFromCsv("C:\\Users\\Brutalocalypse\\Desktop\\adc_test_1.csv", true);

            using (var fs = File.OpenRead(@"C:\Users\LethalInjection\Desktop\adc_test_1.csv"))
            using (var reader = new StreamReader(fs))
            {
                List<string> iter = new List<string>();
                List<string> inVolt = new List<string>();
                List<string> voltX = new List<string>();
                List<string> ampY = new List<string>();
                while (!reader.EndOfStream)
                {
                    var line = reader.ReadLine();
                    var values = line.Split(',');

                    iter.Add(values[0]);
                    inVolt.Add(values[1]);
                    voltX.Add(values[2]);
                    ampY.Add(values[3]);
                }
                this.VoltGraph.Series["Series1"].Points.DataBindXY(iter,inVolt);
            }


            //this.VoltGraph.Series["Series1"].Points.;
            
        }

        private void Refresh_Graph_Click(object sender, EventArgs e)
        {
            this.VoltGraph.Series["Series1"].Points.AddXY("pizza", "33");
            this.VoltGraph.Series["Series1"].Points.AddXY("pie", "44");
            this.VoltGraph.Series["Series1"].Points.AddXY("piz", "55");
            this.VoltGraph.Series["Series1"].Points.AddXY("za", "66");

        }

        private void Clear_Graph_Click(object sender, EventArgs e)
        {
            this.VoltGraph.Series["Series1"].Points.Clear(); // clears only data points
                                                             //this.VoltGraph.Series.Clear(); // wipes the whole dang chart format
                                                             // this.VoltGraph.Series.Add("Series1"); // returns to default layout which is a bar graph
        }

        //static DataTable GetDataTableFromCsv(string path, bool isFirstRowHeader)
        //{
        //    string header = isFirstRowHeader ? "Yes" : "No";

        //    string pathOnly = Path.GetDirectoryName(path);
        //    string fileName = Path.GetFileName(path);

        //    string sql = @"SELECT * FROM [" + fileName + "]";

        //    using (OleDbConnection connection = new OleDbConnection(
        //              @"Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + pathOnly +
        //              ";Extended Properties=\"Text;HDR=" + header + "\""))
        //    using (OleDbCommand command = new OleDbCommand(sql, connection))
        //    using (OleDbDataAdapter adapter = new OleDbDataAdapter(command))
        //    {
        //        DataTable dataTable = new DataTable();
        //        dataTable.Locale = CultureInfo.CurrentCulture;
        //        adapter.Fill(dataTable);
        //        return dataTable;
        //    }
        //}
        //public static System.Data.DataTable ConvertCSVtoDataTable(string strFilePath)
        //{
        //    System.IO.StreamReader sr = new System.IO.StreamReader(strFilePath);
        //    string[] headers = sr.ReadLine().Split(',');
        //    System.Data.DataTable dt = new System.Data.DataTable();
        //    foreach (string header in headers)
        //    {
        //        dt.Columns.Add(header);
        //    }
        //    while (!sr.EndOfStream)
        //    {
        //        string[] rows = System.Text.RegularExpressions.Regex.Split(sr.ReadLine(), ",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)");
        //        System.Data.DataRow dr = dt.NewRow();
        //        for (int i = 0; i < headers.Length; i++)
        //        {
        //            dr[i] = rows[i];
        //        }
        //        dt.Rows.Add(dr);
        //        //}
        //        //return dt;
        //    }
        //}


        // State object for receiving data from remote device.  
        public class StateObject
        {
            // Client socket.  
            public Socket workSocket = null;
            // Size of receive buffer.  
            public const int BufferSize = 20;
            // Receive buffer.  
            public byte[] buffer = new byte[BufferSize];
            // Received data string.  
            public StringBuilder sb = new StringBuilder();
        }

        public class AsynchronousClient
        {
            // The port number for the remote device.  
            private const int port = 50525;

            // ManualResetEvent instances signal completion.  
            private static ManualResetEvent connectDone =
                new ManualResetEvent(false);
            private static ManualResetEvent sendDone =
                new ManualResetEvent(false);
            private static ManualResetEvent receiveDone =
                new ManualResetEvent(false);

            // The response from the remote device.  
            private static String response = String.Empty;

            //public static void StartClient()
            public static int StartClient(decimal input0, decimal input1, decimal input2, decimal input3)
            {
                // Connect to a remote device.  
                try
                {
                    // Establish the remote endpoint for the socket.  
                    // The name of the   
                    // remote device is "host.contoso.com".  
                    //IPHostEntry ipHostInfo = Dns.Resolve("host.contoso.com");
                    IPAddress ipAddress = IPAddress.Parse("192.168.137.251");
                    IPEndPoint remoteEP = new IPEndPoint(ipAddress, port);

                    // Create a TCP/IP socket.  
                    Socket client = new Socket(AddressFamily.InterNetwork,
                        SocketType.Stream, ProtocolType.Tcp);

                    // Connect to the remote endpoint.  
                    client.BeginConnect(remoteEP,
                        new AsyncCallback(ConnectCallback), client);
                    connectDone.WaitOne();

                    // Send test data to the remote device.


                    //
                    string[] data = new string[4];
                    string specifier = "G";
                    data[0] = input0.ToString(specifier);
                    data[1] = input1.ToString(specifier);
                    data[2] = input2.ToString(specifier);
                    data[3] = input3.ToString(specifier);
                    string sendOff = $"demo2: {data[0]} {data[1]} {data[2]} {data[3]} \n";

                    Console.WriteLine(data[0]);
                    Console.WriteLine(data[1]);
                    Console.WriteLine(data[2]);
                    Console.WriteLine(data[3]);
                    Console.WriteLine(sendOff);


                    Send(client, sendOff);
                    //Send(client, "pwm: 0 0.4 0 0 \n");

                    sendDone.WaitOne();

                    // Receive the response from the remote device.  
                    Receive(client);
                    receiveDone.WaitOne();

                    // Write the response to the console.  
                    Console.WriteLine("Response received : {0}", response);

                    // Release the socket.  
                    client.Shutdown(SocketShutdown.Both);
                    client.Close();

                }
                catch (Exception e)
                {
                    Console.WriteLine(e.ToString());
                }
                return 0;
            }

            private static void ConnectCallback(IAsyncResult ar)
            {
                try
                {
                    // Retrieve the socket from the state object.  
                    Socket client = (Socket)ar.AsyncState;

                    // Complete the connection.  
                    client.EndConnect(ar);

                    Console.WriteLine("Socket connected to {0}",
                        client.RemoteEndPoint.ToString());

                    // Signal that the connection has been made.  
                    connectDone.Set();
                }
                catch (Exception e)
                {
                    Console.WriteLine(e.ToString());
                }
            }

            private static void Receive(Socket client)
            {
                try
                {
                    // Create the state object.  
                    StateObject state = new StateObject();
                    state.workSocket = client;

                    // Begin receiving the data from the remote device.  
                    client.BeginReceive(state.buffer, 0, StateObject.BufferSize, 0,
                        new AsyncCallback(ReceiveCallback), state);
                }
                catch (Exception e)
                {
                    Console.WriteLine(e.ToString());
                }
            }

            private static void ReceiveCallback(IAsyncResult ar)
            {
                try
                {
                    // Retrieve the state object and the client socket   
                    // from the asynchronous state object.  
                    StateObject state = (StateObject)ar.AsyncState;
                    Socket client = state.workSocket;

                    // Read data from the remote device.  
                    int bytesRead = client.EndReceive(ar);

                    if (bytesRead > 0)
                    {
                        // There might be more data, so store the data received so far.  
                        state.sb.Append(Encoding.ASCII.GetString(state.buffer, 0, bytesRead));

                        // Get the rest of the data.  
                        client.BeginReceive(state.buffer, 0, StateObject.BufferSize, 0,
                            new AsyncCallback(ReceiveCallback), state);
                    }
                    else
                    {
                        // All the data has arrived; put it in response.  
                        if (state.sb.Length > 1)
                        {
                            response = state.sb.ToString();
                        }
                        // Signal that all bytes have been received.  
                        receiveDone.Set();
                    }
                }
                catch (Exception e)
                {
                    Console.WriteLine(e.ToString());
                }
            }

            private static void Send(Socket client, String data)
            {
                // Convert the string data to byte data using ASCII encoding.  
                byte[] byteData = Encoding.ASCII.GetBytes(data);

                // Begin sending the data to the remote device.  
                client.BeginSend(byteData, 0, byteData.Length, 0,
                    new AsyncCallback(SendCallback), client);
            }

            private static void SendCallback(IAsyncResult ar)
            {
                try
                {
                    // Retrieve the socket from the state object.  
                    Socket client = (Socket)ar.AsyncState;

                    // Complete sending the data to the remote device.  
                    int bytesSent = client.EndSend(ar);
                    Console.WriteLine("Sent {0} bytes to server.", bytesSent);

                    // Signal that all bytes have been sent.  
                    sendDone.Set();
                }
                catch (Exception e)
                {
                    Console.WriteLine(e.ToString());
                }
            }

            //public static int Main(String[] args)
            //{
            //    StartClient();
            //     return 0;
            //}
        }

    }
}