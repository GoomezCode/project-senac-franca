package searchGroup;

import java.awt.*;
import java.util.*;

public class entityGroup {
	private int id;
	private String nome;
	private int ponto;
// ------------------------------------------------	
	public ArrayList<entityGroup> getAllGroup(ArrayList<entityGroup> groups){
		ArrayList<entityGroup> bugFix = new ArrayList<entityGroup>();
		ArrayList<Integer> ids = new ArrayList<Integer>();
		for(entityGroup group: groups) {
			entityGroup newGroup = new entityGroup();
			int ponto = group.getPonto();
			for (entityGroup listVerific: groups) {
				if(group.getId() == listVerific.getId()) {
					continue;
				}
				if (group.getNome().equalsIgnoreCase(listVerific.getNome())) {
						ponto += listVerific.getPonto();
				}

			}
			newGroup.setId(group.id);
			newGroup.setNome(group.getNome());
			newGroup.setPonto(ponto);
			bugFix.add(newGroup);
		}
		return bugFix;
	}

	public String[] getGroup(String nome, ArrayList<entityGroup> groups){
		String[] group = new String[2];
		for(entityGroup group1: groups) {
			if(nome.toLowerCase().equals(group1.getNome().toLowerCase())) {
				group[0] = group1.getNome();
				group[1] = String.valueOf(group1.getPonto());
			}else{continue;}
		}
		return group;
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
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
}
