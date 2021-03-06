package threadChat;

import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;
import java.util.List;

public class Server {
	private ServerSocket server;
	private InputListener input;
	//private ObjectInputStream input;
	private ObjectOutputStream output;
	private List<Socket> clients;
	private List<ObjectOutputStream> outputs;
	private List<InputListener> inputs;
	
	public Server(int porta) throws IOException {
		// Instancia das lists
		clients = new ArrayList<Socket>();
		outputs = new ArrayList<ObjectOutputStream>();
		inputs = new ArrayList<InputListener>();
		
		server = new ServerSocket(porta);
		ConnectionListener conn = ConnectionListener.instance(this);
	}
	
	/*public Socket connect(int porta) throws IOException {
		server = new ServerSocket(porta);
		Socket client = server.accept();
		output = new ObjectOutputStream(client.getOutputStream());
		input = new InputListener(client.getInputStream());
		//input = new ObjectInputStream(client.getInputStream());
		return client;
	}*/
	public void addClient(Socket client) {
		clients.add(client);
		try {
			outputs.add(new ObjectOutputStream(client.getOutputStream()));
			inputs.add(new InputListener(client.getInputStream()));
			
			System.out.println("New client connected...\n");
		}catch(IOException e) {
			clients.remove(client);
			e.printStackTrace();
		}
	}
	
	public void send(String string) throws IOException{
		for(ObjectOutputStream output:outputs) {
			output.writeUTF(string);
			output.flush();
		}
	}
	
//	public String receive() throws IOException{
//		return input.readUTF();
//	}
	
	public void disconnect(Socket socket) throws IOException {
		input.close();
		output.close();
		socket.close();
	}
	
	public ServerSocket getServer() {
		return server;
	}
}
