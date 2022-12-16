package com.adm.scheduler;

import org.quartz.*;
import org.quartz.impl.StdSchedulerFactory;

public class main {
    public static void main (String[] args) throws InterruptedException {
        SchedulerFactory factory = new StdSchedulerFactory();
        JobDetail job = JobBuilder.newJob(SimpleJob.class)
                .withIdentity("First Job", "G1")
                .usingJobData("IdMap", "yId")
                .build();
        Trigger trigger = TriggerBuilder.newTrigger()
                .withIdentity("First trigger", "T1")
                .startNow()
                .withSchedule(SimpleScheduleBuilder.simpleSchedule()
                        .withIntervalInSeconds(2)
                        .repeatForever()).build();
        try {
            Scheduler scheduler = factory.getScheduler();
            if (!scheduler.checkExists(job.getKey())) {
                scheduler.scheduleJob(job, trigger);
            }
            scheduler.start();
        } catch (SchedulerException e) {
            throw new RuntimeException(e);
        }

    }
}
