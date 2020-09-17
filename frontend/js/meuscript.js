$(function() { // quando o documento estiver pronto/carregado
    
    // função para exibir pessoas na tabela
        $.ajax({
            url: 'http://localhost:5000/listar_roupas',
            method: 'GET',
            dataType: 'json',
            success: listar,
            error: function() {
                alert("erro ao ler dados, verifique o backend");
            }
        });

        function listar (roupas) {
        
            for (var i in roupas) { //i vale a posição no vetor
                lin = '<tr>' + 
                '<td>' + roupas[i].id + '</td>' + 
                '<td>' + roupas[i].modelo + '</td>' + 
                '<td>' + roupas[i].tamanho + '</td>' +
                '<td>' + roupas[i].cor + '</td>' +
                '<td>' + roupas[i].tecido + '</td>' +
                '<td>' + roupas[i].marca + '</td>' +
                '</tr>';
        
                // adiciona a linha no corpo da tabela

                $('#corpoTabelaRoupas').append(lin);
            }
            
        }
    });
