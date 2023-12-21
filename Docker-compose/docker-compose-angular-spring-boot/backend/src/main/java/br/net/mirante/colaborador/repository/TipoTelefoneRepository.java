package br.net.mirante.colaborador.repository;

import br.net.mirante.colaborador.domain.model.TipoTelefone;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface TipoTelefoneRepository extends JpaRepository<TipoTelefone, Long> {
}
