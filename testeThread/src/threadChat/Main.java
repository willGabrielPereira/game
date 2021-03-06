package threadChat;

import java.io.IOException;
import java.net.InetAddress;
import java.net.Socket;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);

		System.out.print("Select 1 to host or 2 to client: ");
		int num = Integer.parseInt(scan.nextLine());
		
		switch(num) {
		case 1:
			Server server;
			Socket host;
			try {
				String ip = InetAddress.getLocalHost().getHostAddress();
				System.out.println("Your IP: "+ip);
				
				server = new Server(6565);
				System.out.println("Waiting connection...");
				//host = server.connect(6565);
				//System.out.println("Client connected...");
				
				String message = "";
				
				while(!message.equals("exit")){
					message = scan.nextLine();
					server.send(message);
				}
				

				System.out.println("System disconnecting");
				//server.disconnect(host);
				
			}catch(IOException e) {
				System.out.println("Error: "+e);
			}
			break;
		case 2:
			System.out.print("Insert host IP: ");
			String hostIp = scan.nextLine();
			Client client;
			try {
				client = new Client(hostIp, 6565);
				String message = "";
				while(!message.equals("exit")){
					String send = scan.nextLine();
					client.send(send);
					//message = client.receive();
				}
				

				System.out.println("System disconnecting");
				client.disconnect();
			}catch(IOException e) {
				System.out.println("Error: "+e);
			}
			break;
		}
		
		scan.close();

	}


}
