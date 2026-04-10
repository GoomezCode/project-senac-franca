package searchGroup;

import java.util.ArrayList;
import java.util.Iterator;

public class entityGroup {
	private String nome;
	private int ponto;
// ------------------------------------------------	
	public static ArrayList<entityGroup> getGroup(ArrayList<entityGroup> groups){
		ArrayList<entityGroup> bugFix = new ArrayList<entityGroup>();
		for(entityGroup group: groups) {
			entityGroup newGroup = new entityGroup();
			int ponto = group.getPonto();
			
			for (int i = 1; i < groups.size(); i++) {
				if (group.getNome() == groups.get(i).getNome()) {
					ponto += groups.get(i).getPonto();
				}
			}
			
			newGroup.setNome(group.getNome());
			newGroup.setPonto(ponto);
			bugFix.add(newGroup);
		}
		
	return bugFix;
}
	
// ------------------------------------------------
	public String getNome() {
		return nome;
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
	public int getPonto() {
		return ponto;
	}
	public void setPonto(int ponto) {
		this.ponto = ponto;
	}
}
