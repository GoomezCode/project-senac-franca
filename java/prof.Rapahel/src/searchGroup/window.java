package searchGroup;

import java.util.ArrayList;
import java.util.Iterator;
public class window {
public static void main(String[] args) {
	ArrayList<entityGroup> groups = new ArrayList<entityGroup>();
	for(int i = 0; i <10; i++) {
		entityGroup group = new entityGroup();
		group.setNome("Grupo-"+(i+1));
		group.setPonto( (int) Math.round(Math.random()*9));
		groups.add(group);
	}
	
	for(int i = 0; i < new entityGroup().getGroup(groups).size();i++) {
		
		System.out.println(new entityGroup().getGroup(groups).get(i).getNome());
		System.out.println(new entityGroup().getGroup(groups).get(i).getPonto());
	}
	
}
}
