package threadChat;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class ConnectionListener extends Thread{
	private ServerSocket server;
	
	public ConnectionListener(ServerSocket server) {
		this.server = server;
		start();
	}
	
	public void run() {
		try {
			Socket client = server.accept();
			// chamar addClient da classe Server
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}
