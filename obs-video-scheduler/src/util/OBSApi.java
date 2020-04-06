package util;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Properties;
import java.util.Scanner;

import org.apache.thrift.TException;
import org.apache.thrift.protocol.TBinaryProtocol;
import org.apache.thrift.protocol.TProtocol;
import org.apache.thrift.transport.TSSLTransportFactory;
import org.apache.thrift.transport.TSocket;
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.TSSLTransportFactory.TSSLTransportParameters;

import scheduler.ObsThriftServer;

public class OBSApi {
	ObsThriftServer.Client client;
	TTransport transport;
	
	public OBSApi() {
		try {
			transport = new TSocket(Config.getOBSHost(), 9090);
			transport.open();
			TProtocol protocol = new TBinaryProtocol(transport);
			client = new ObsThriftServer.Client(protocol);
		} catch (Exception x) {
			x.printStackTrace();
		}
	}

	public void launchVideoByPath(String filePath, String name, List<String> toMute) throws FileNotFoundException, IOException {
//		try {
//			client.l
//			transport.close();
//		} catch (TException e) {
//			e.printStackTrace();
//		}
	}

	public void removeSource(String name, List<String> toUnMute) throws IOException {
//		try {
//			client.removeSource(name, toUnMute);
//			transport.close();
//		} catch (TException e) {
//			e.printStackTrace();
//		}
	}

	public void close() {
		//transport.close();
	}
}
 