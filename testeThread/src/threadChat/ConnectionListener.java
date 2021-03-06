package threadChat;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class ConnectionListener extends Thread{
	private static ConnectionListener conn;
	private ServerSocket server;
	private Server host;
	
	private ConnectionListener(Server server) {
		this.host = server;
		this.server = server.getServer();
		start();
	}
	
	public static ConnectionListener instance(Server server) {
		if(conn == null) {
			return new ConnectionListener(server);
		}
		return conn;
	}
	
	public void run() { 
		try {
			Socket client = server.accept();
			System.out.println("Recebi\n\n");
			host.addClient(client);
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}
