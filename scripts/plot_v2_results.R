#!/usr/bin/env Rscript
# Reproduce measured BIPT v2.0 figures. No simulated observations or uncertainty.
# Preserve Unicode project paths when the launching shell inherits a C locale.
if(Sys.getlocale('LC_CTYPE') %in% c('C','POSIX')) {
 for(loc in c('C.UTF-8','en_US.UTF-8','UTF-8')) {
  chosen <- suppressWarnings(Sys.setlocale('LC_CTYPE',loc))
  if(nzchar(chosen))break
 }
}
suppressPackageStartupMessages({library(ggplot2);library(grid);library(svglite);library(ggrepel);library(ragg)})
args <- commandArgs(trailingOnly=FALSE)
self <- sub('^--file=', '', args[grepl('^--file=', args)])
root <- normalizePath(file.path(dirname(self), '..'))
results <- file.path(root, 'results', 'v2')
out <- file.path(root, 'figures', 'v2'); dir.create(out, recursive=TRUE, showWarnings=FALSE)
d <- read.csv(file.path(results,'leaderboard.csv'), stringsAsFactors=FALSE, na.strings=c('','NA'))
cases <- read.csv(file.path(results,'case_scores.csv'), stringsAsFactors=FALSE)
stopifnot(nrow(d)>=2L, !anyDuplicated(d$configuration_id), all(is.na(d$total) | d$total>=0 & d$total<=100), all(d$credits>=0))
stopifnot(nrow(d)==8L, all(d$status=='completed_scored'))
phases <- read.csv(file.path(results,'execution_phases.csv'),stringsAsFactors=FALSE)
completed <- d$status=='completed_scored'
d$display <- d$model
d$display[d$role=='development_calibration_baseline'] <- paste0(d$model[d$role=='development_calibration_baseline'],' *')
d$display[d$role=='completion_after_external_interruption'] <- paste0(d$model[d$role=='completion_after_external_interruption'],' +')
d <- d[order(!completed, -ifelse(is.na(d$total),-1,d$total),d$configuration_id),]
levels_model <- rev(d$display)
d$display <- factor(d$display, levels=levels_model)
font <- 'Helvetica'
theme_set(theme_classic(base_size=8, base_family=font)+theme(
  axis.title=element_text(size=8),axis.text=element_text(size=7),legend.title=element_text(size=7),legend.text=element_text(size=7),
  plot.title=element_text(size=9,face='bold'),plot.subtitle=element_text(size=7),plot.caption=element_text(size=6.5,hjust=0),
  axis.line=element_line(linewidth=.3),axis.ticks=element_line(linewidth=.3),legend.position='top',
  plot.margin=margin(4,8,4,4,'mm')))
component_cols <- c(Numerical='#3C5488',Scientific='#E64B35',Delivery='#A0A0A0')
long <- do.call(rbind,lapply(seq_len(nrow(d)),function(i) {
 data.frame(display=d$display[i], component=factor(c('Numerical','Scientific','Delivery'),levels=c('Numerical','Scientific','Delivery')),
            points=c(d$numerical[i],d$scientific[i],d$delivery[i]),status=d$status[i])
}))
long$display <- factor(long$display,levels=levels_model)
pa <- ggplot(long[long$status=='completed_scored',],aes(x=points,y=display,fill=component))+
 geom_col(width=.64,position=position_stack(reverse=TRUE))+
 geom_text(data=d[d$status=='completed_scored',],aes(x=total+1.4,y=display,label=sprintf('%.2f',total)),inherit.aes=FALSE,hjust=0,size=2.5,family=font)+
 geom_text(data=d[d$status!='completed_scored',],aes(x=4,y=display,label='Incomplete - no completed score'),inherit.aes=FALSE,hjust=0,size=2.5,family=font,colour='#666666')+
 scale_fill_manual(values=component_cols,drop=FALSE)+scale_x_continuous(limits=c(0,108),breaks=seq(0,100,25),expand=expansion(mult=c(0,0)))+
 scale_y_discrete(limits=levels_model,drop=FALSE)+
 labs(title='a  Frozen-task score and its components',x='Weighted points (maximum 100)',y=NULL,fill=NULL)+
 theme(axis.line.y=element_blank(),axis.ticks.y=element_blank())
case_levels <- c('Released','Held-out 1','Held-out 2')
map <- c(public='Released',hidden1='Held-out 1',hidden2='Held-out 2')
full <- expand.grid(configuration_id=d$configuration_id,case=names(map),stringsAsFactors=FALSE)
full <- merge(full,cases,by=c('configuration_id','case'),all.x=TRUE,sort=FALSE)
full$display <- factor(as.character(d$display[match(full$configuration_id,d$configuration_id)]),levels=levels_model)
full$case_display <- factor(unname(map[full$case]),levels=case_levels)
full$label <- ifelse(is.na(full$total),'NA',paste0(formatC(full$total,format='f',digits=2),ifelse(full$returncode!=0,' !','')))
full$textcolour <- ifelse(is.na(full$total)|full$total<65,'#222222','white')
pb <- ggplot(full,aes(x=case_display,y=display,fill=total))+geom_tile(width=.93,height=.85)+
 geom_text(aes(label=label,colour=textcolour),size=2.5,family=font,show.legend=FALSE)+scale_colour_identity()+
 scale_fill_gradient(low='#F1F4F7',high='#2166AC',limits=c(0,100),na.value='#DDDDDD',name='Case score')+
 scale_y_discrete(limits=levels_model,drop=FALSE)+
 labs(title='b  Transfer across the same three cases',x=NULL,y=NULL,
      caption='! Non-zero entry exit; correctly delivered partial results retain their frozen points. All generation tasks reached normal service completion.')+
 theme(axis.line=element_blank(),axis.ticks=element_blank(),legend.position='right')
# Preserve exact single-run observations: no error bars or confidence intervals are estimated.
foot <- '* Development Flash baseline (task-selection bias). + Resumed original task with neutral continuation; not independent repeats.'
draw_grid <- function(plots,heights,title,footnote) {
 grid.newpage();pushViewport(viewport(layout=grid.layout(length(plots)+2,1,heights=unit(c(.10,heights,.12),'null'))))
 grid.text(title,x=.01,y=.5,just='left',vp=viewport(layout.pos.row=1),gp=gpar(fontsize=10,fontface='bold',fontfamily=font))
 for(i in seq_along(plots))print(plots[[i]],vp=viewport(layout.pos.row=i+1))
 grid.text(footnote,x=.01,y=.5,just='left',vp=viewport(layout.pos.row=length(plots)+2),gp=gpar(fontsize=6.5,fontfamily=font))
 popViewport()
}
export <- function(stem,plots,heights,title,footnote,width_mm=183,height_mm=180) {
 width <- width_mm/25.4;height <- height_mm/25.4
 # Base R PDF keeps editable Helvetica text and does not require optional XQuartz libraries.
 # Cairo PDF is available on hosts that explicitly enable a working Cairo device.
 if(identical(Sys.getenv('BIPT_USE_CAIRO'),'1')) {
  grDevices::cairo_pdf(file.path(out,paste0(stem,'.pdf')),width=width,height=height,family=font,onefile=FALSE)
 } else {
  grDevices::pdf(file.path(out,paste0(stem,'.pdf')),width=width,height=height,family=font,useDingbats=FALSE,onefile=FALSE)
 }
 draw_grid(plots,heights,title,footnote);dev.off()
 svglite::svglite(file.path(out,paste0(stem,'.svg')),width=width,height=height,bg='white')
 draw_grid(plots,heights,title,footnote);dev.off()
 ragg::agg_png(file.path(out,paste0(stem,'.png')),width=width_mm,height=height_mm,units='mm',res=600,background='white')
 draw_grid(plots,heights,title,footnote);dev.off()
}
export('score_and_case_comparison',list(pa,pb),c(.9,.9),'BIPT v2.0 | Single-run WorkBuddy comparison',foot,height_mm=max(155,95+9*nrow(d)))
# Matched case differences use only within-provider configurations on the same frozen cases.
pairs <- list(DeepSeek=c('DeepSeek-V4-Pro','DeepSeek-V4.1-Flash'),GLM=c('GLM-5.3','GLM-5.3-Flash'),MiniMax=c('MiniMax-M3','MiniMax-M3.1-Flash'))
pairrows <- list()
for(fam in names(pairs)) {
 a <- d[d$model==pairs[[fam]][1] & d$status=='completed_scored',];b <- d[d$model==pairs[[fam]][2] & d$status=='completed_scored',]
 if(nrow(a)!=1 || nrow(b)!=1)next
 for(case in names(map)) {
  aa <- cases[cases$configuration_id==a$configuration_id & cases$case==case,];bb <- cases[cases$configuration_id==b$configuration_id & cases$case==case,]
  stopifnot(nrow(aa)==1,nrow(bb)==1)
  pairrows[[length(pairrows)+1]] <- data.frame(family=fam,premium_model=a$model,flash_model=b$model,case=case,premium_score=aa$total,flash_score=bb$total,difference=aa$total-bb$total)
 }
}
provider_cols <- c(DeepSeek='#3C5488',GLM='#00A087',MiniMax='#7E6148',Xiaomi='#E64B35',Step='#8C6BB1',Kimi='#4DBBD5')
if(length(pairrows)) {
 pd <- do.call(rbind,pairrows);pd$case_display <- factor(unname(map[pd$case]),levels=case_levels)
 write.csv(pd,file.path(results,'within_family_case_differences.csv'),row.names=FALSE,na='')
 pc <- ggplot(pd,aes(x=case_display,y=difference,colour=family,group=family))+
  geom_hline(yintercept=0,linewidth=.35,linetype='dashed',colour='#777777')+geom_line(linewidth=.55)+geom_point(size=2)+
  scale_colour_manual(values=provider_cols)+labs(title='a  Matched-case configuration differences',x=NULL,y='Standard/Pro minus Flash (points)',colour='Provider',
  subtitle='Different version labels within DeepSeek and MiniMax; these are not pure speed-tier ablations.')
} else {
 pc <- ggplot()+annotate('text',x=0,y=0,label='No finalized within-provider pair yet',family=font,size=3)+theme_void()
}
resource <- d[d$status=='completed_scored',]
short <- c('DeepSeek-V4-Pro'='DeepSeek Pro','DeepSeek-V4.1-Flash'='DeepSeek Flash *','GLM-5.3'='GLM','GLM-5.3-Flash'='GLM Flash','MiniMax-M3'='MiniMax M3','MiniMax-M3.1-Flash'='MiniMax Flash','Xiaomi MiMo-V2.6-Pro'='MiMo Pro','Step-5-Preview'='Step','Kimi-K3.1-Pro'='Kimi Pro')
resource$short <- unname(short[resource$model]);resource$short[is.na(resource$short)]<-resource$model[is.na(resource$short)]
resource$short[resource$role=='completion_after_external_interruption'] <- paste0(resource$short[resource$role=='completion_after_external_interruption'],' +')
resource$label <- paste0(resource$short,'\n',round(resource$elapsed_seconds/60,1),' min')
resource$baseline <- resource$role=='development_calibration_baseline'
pr <- ggplot(resource,aes(x=credits,y=total,colour=family))+geom_point(aes(shape=baseline),size=2.2,stroke=.8)+
 ggrepel::geom_text_repel(aes(label=label),family=font,size=2.4,min.segment.length=0,seed=20261118,box.padding=.4,max.overlaps=Inf,show.legend=FALSE)+
 scale_shape_manual(values=c('FALSE'=16,'TRUE'=1),guide='none')+scale_colour_manual(values=provider_cols)+
 scale_y_continuous(limits=c(-4,108),breaks=seq(0,100,25))+expand_limits(x=0)+
 labs(title='b  Observed service cost and elapsed time',x='Actual WorkBuddy credits',y='Weighted score / 100',colour='Provider',
 subtitle='Total initial + continuation credits; durations are displayed service time, not matched compute.')
export('paired_and_resource_comparison',list(pc,pr),c(.75,1),'BIPT v2.0 | Configuration contrasts and resources',foot,height_mm=160)
resource_all <- do.call(rbind,lapply(seq_len(nrow(d)),function(i) {
 ph <- phases[phases$configuration_id==d$configuration_id[i],];stopifnot(nrow(ph)==1L)
 data.frame(display=d$display[i],metric=factor(rep(c('a  Actual WorkBuddy credits','b  Service elapsed minutes'),each=2),levels=c('a  Actual WorkBuddy credits','b  Service elapsed minutes')),
            value=c(ph$initial_credits,ph$continuation_credits,ph$initial_elapsed_seconds/60,ph$continuation_elapsed_seconds/60),
            phase=factor(rep(c('Initial generation','Neutral continuation'),2),levels=c('Initial generation','Neutral continuation')))
}))
resource_all$display <- factor(resource_all$display,levels=levels_model)
resource_totals <- aggregate(value~display+metric,resource_all,sum)
resource_totals$label <- ifelse(resource_totals$metric=='a  Actual WorkBuddy credits',sprintf('%.2f',resource_totals$value),sprintf('%.1f',resource_totals$value))
px <- ggplot(resource_all,aes(x=value,y=display,fill=phase))+geom_col(width=.65,position=position_stack(reverse=TRUE))+
 geom_text(data=resource_totals,inherit.aes=FALSE,mapping=aes(x=value,y=display,label=label),hjust=-.1,family=font,size=2.4)+facet_wrap(~metric,nrow=1,scales='free_x')+
 scale_fill_manual(values=c('Initial generation'='#3C5488','Neutral continuation'='#E64B35'))+
 scale_y_discrete(limits=levels_model,drop=FALSE)+
 scale_x_continuous(expand=expansion(mult=c(0,.22)))+
 labs(title='All configurations completed; initial and resumed resource use',x=NULL,y=NULL,fill=NULL,
      caption='Final segment bills and displayed service durations are summed. Idle calendar time may be excluded.')+
 theme(axis.line.y=element_blank(),axis.ticks.y=element_blank(),strip.background=element_blank(),strip.text=element_text(size=8,face='bold'),legend.position='top')
export('execution_resources',list(px),c(1),'BIPT v2.0 | Initial and continuation resources',foot,height_mm=max(105,65+7*nrow(d)))
cat('Rendered finalized data only:',nrow(d),'configurations;',nrow(cases),'case rows\n')
