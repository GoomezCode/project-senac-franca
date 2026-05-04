package searchGroup;

import java.util.ArrayList;
import java.util.LinkedHashSet;
import java.util.List;

public class window {
	public static entityGroup getGroups = new entityGroup();
	public static ArrayList<entityGroup> groups = new ArrayList<entityGroup>();
public static void main(String[] args) {

	for(int i = 0; i <5; i++) {
		entityGroup group = new entityGroup();
		group.setId(i+1);
		group.setNome("Grupo-"+(int) Math.round(Math.random()*10));
		group.setPonto( (int) Math.round(Math.random()*9));
		groups.add(group);
	}

	System.out.println(getAllGroups());
}

	public static StringBuilder getAllGroups() {
		StringBuilder window = new  StringBuilder();
		ArrayList<String> ordenar = new  ArrayList<>();
		for(entityGroup group : getGroups.getAllGroup(groups)) {
			ordenar.add(group.getNome());
		}
		List<String> listaSemDuplicados = new ArrayList<>(new LinkedHashSet<>(ordenar));
		for (String org: listaSemDuplicados) {
			String[] group = getGroups.getGroup(org, getGroups.getAllGroup(groups));
			window.append("\n");
			window.append("\n Nome: "+ group[0]);
			window.append("\n ponto: "+group[1]);
		}
		return window;
	}

	public static StringBuilder getGroup(String nome) {
	StringBuilder window = new  StringBuilder();
	String[] group = getGroups.getGroup(nome, getGroups.getAllGroup(groups));
	if(group[0] == null) {
		window.append("\n Grupo não encontrado!!");
	}else{
		window.append("\n Nome: "+group[0]);
		window.append("\n Ponto: "+group[1]);
	}

	return window;
	}

}
