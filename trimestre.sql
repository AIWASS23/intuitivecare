-- Top 10 Operadoras com Maiores Despesas no Último Trimestre

SELECT 
    o.registro_ans, 
    o.razao_social, 
    SUM(d.vl_saldo_final) AS total_despesas
FROM 
    demonstracoes_contabeis d
JOIN 
    operadoras o ON d.reg_ans = o.registro_ans
WHERE 
    d.descricao ILIKE '%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%'
    AND d.data >= '2024-10-01'  
    AND d.data <= '2024-12-31' 
GROUP BY 
    o.registro_ans, o.razao_social
ORDER BY 
    total_despesas DESC
LIMIT 10;

/*

registro_ans |                       razao_social                       | total_despesas 
--------------+----------------------------------------------------------+----------------
 326305       | AMIL ASSISTÊNCIA MÉDICA INTERNACIONAL S.A.               | 20820818085.36
 359017       | NOTRE DAME INTERMÉDICA SAÚDE S.A.                        |  9307980465.62
 368253       | HAPVIDA ASSISTENCIA MEDICA S.A.                          |  7755562753.15
 346659       | CAIXA DE ASSISTÊNCIA DOS FUNCIONÁRIOS DO BANCO DO BRASIL |  7459368017.21
 339679       | UNIMED NACIONAL - COOPERATIVA CENTRAL                    |  7002487899.10
 302147       | PREVENT SENIOR PRIVATE OPERADORA DE SAÚDE LTDA           |  5920615078.62
 343889       | UNIMED BELO HORIZONTE COOPERATIVA DE TRABALHO MÉDICO     |  5411476065.42
 323080       | GEAP AUTOGESTÃO EM SAÚDE                                 |  3435605702.55
 352501       | UNIMED PORTO ALEGRE - COOPERATIVA MÉDICA LTDA.           |  3368044333.04
 335690       | UNIMED CAMPINAS - COOPERATIVA DE TRABALHO MÉDICO         |  3059368303.48

*/