# 1) Gráfico do valor da cpu sem a média do valor por minuto
cpu_temp_25 <- subset(cpu_temp, dataHora >= "2023-10-25 00:00:00" & dataHora <= "2023-10-25 23:59:59")
barplot(cpu_temp_25$valor,
        names.arg = cpu_temp_25$dataHora,
        xlab = "Data/Hora",
        ylab = "Valor do uso da CPU",
        main = "Valor do uso da CPU x Data/Hora do uso (dia 25)",
        cex.axis = 0.75,
        las = 1
)

# 2) Média do valor da cpu de cada minuto por hora
cpu_temp_25$hora <- hour(cpu_temp_25$dataHora)
cpu_temp_25$minuto <- minute(cpu_temp_25$dataHora)
cpu_temp_25_grouped <- split(cpu_temp_25, list(cpu_temp_25$hora, cpu_temp_25$minuto))
cpu_temp_25_mean <- sapply(cpu_temp_25_grouped, function(x) mean(x$valor))
barplot(cpu_temp_25_mean,
        col = "blue",
        xlab = "Hora:Minuto",
        ylab = "Média do uso da CPU",
        main = "Média do uso da CPU por minuto de cada hora no dia 25/10/2023",
        cex.axis = 0.75,
        las = 2
)

# 3) Média do valor da cpu por hora
cpu_temp_25$hora <- hour(cpu_temp_25$dataHora)
cpu_temp_25_grouped <- split(cpu_temp_25, cpu_temp_25$hora)
cpu_temp_25_mean <- sapply(cpu_temp_25_grouped, function(x) mean(x$valor))
barplot(cpu_temp_25_mean,
        col = "blue",
        xlab = "Hora",
        ylab = "Média do uso da CPU",
        main = "Média do uso da CPU por hora no dia 25/10/2023",
        cex.axis = 0.75,
        las = 1
)


# 4) Média do valor da memória de cada minuto por hora
memoria_temp_25$hora <- hour(memoria_temp_25$dataHora)
memoria_temp_25$minuto <- minute(memoria_temp_25$dataHora)

memoria_temp_25_grouped <- split(memoria_temp_25, list(memoria_temp_25$hora, memoria_temp_25$minuto))

memoria_temp_25_mean <- sapply(memoria_temp_25_grouped, function(x) mean(x$valor))

barplot(memoria_temp_25_mean,
        col = "blue",
        xlab = "Hora:Minuto",
        ylab = "Média do uso da memória",
        main = "Média do uso da memória por minuto de cada hora no dia 25/10/2023",
        cex.axis = 0.75,
        las = 2
)


# 5) Média do valor da memória por hora
memoria_temp_25$hora <- hour(memoria_temp_25$dataHora)

memoria_temp_25_grouped <- split(memoria_temp_25, memoria_temp_25$hora)

memoria_temp_25_mean <- sapply(memoria_temp_25_grouped, function(x) mean(x$valor))

barplot(memoria_temp_25_mean,
        col = "blue",
        xlab = "Hora",
        ylab = "Média do uso da memória",
        main = "Média do uso da memória por hora no dia 25/10/2023",
        cex.axis = 0.75,
        las = 1
)



# 6) Filtrar os dados para o dia 26 de outubro
cpu_temp_26 <- subset(cpu_temp, dataHora >= "2023-10-26 00:00:00" & dataHora <= "2023-10-26 23:59:59")
modelo1 <- lm(temperatura ~ valor, data = cpu_temp_26)
ggplot(mapping = aes(x = temperatura, y = valor), data = cpu_temp_26) +
geom_point() +
geom_smooth(method = "lm")


# 7) Filtrar os dados para o dia 26 de outubro
memoria_temp_26 <- subset(memoria_temp, dataHora >= "2023-10-26 00:00:00" & dataHora <= "2023-10-26 23:59:59")
modelo1 <- lm(temperatura ~ valor, data = memoria_temp_26)
ggplot(mapping = aes(x = temperatura, y = valor), data = memoria_temp_26) +
  geom_point() +
  geom_smooth(method = "lm")


